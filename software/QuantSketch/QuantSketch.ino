/*

Dual Quantizer
Rich Holmes 4/2020

Uses dac_ino library to communicate with board and quantize library
to do the quantization, this is just the glue in between...

 */

#include <dac_ino.h>
#include <Quantizer.h>

//  0 - 4095  = 0 - 5V
//  0 - 819   = 0 - 1V
//  68.25 = 1V / 12

#define OCTAVE (4095 / 5)
#define NOTE (OCTAVE / 12)
#define DEBUG true

using namespace di;

Quantizer q[2];

dac_ino::CVInChannel   cv1InChan[2] = {dac_ino::CVInChannel::A, dac_ino::CVInChannel::C};
dac_ino::CVInChannel   cv2InChan[2] = {dac_ino::CVInChannel::B, dac_ino::CVInChannel::D};
dac_ino::CVInChannel   scaleChan[2] = {dac_ino::CVInChannel::H, dac_ino::CVInChannel::F};
dac_ino::CVInChannel   bankChan[2] = {dac_ino::CVInChannel::G, dac_ino::CVInChannel::E};
dac_ino::CVOutChannel  cvOutChan[2] = {dac_ino::CVOutChannel::A, dac_ino::CVOutChannel::B};

dac_ino::GateInChannel quantInChan[2] = {dac_ino::GateInChannel::C, dac_ino::GateInChannel::D};
dac_ino::GateInChannel trigChan[2] = {dac_ino::GateInChannel::A, dac_ino::GateInChannel::B};

bool triggered[2] = {false, false};

unsigned cv[2]; // the CV before quantization
unsigned cvq; // the CV after quantization
unsigned cv2[2]; // transposition CV
unsigned rsbank[2]; // rotary switch states
unsigned rsscale[2]; // rotary switch states
bool     qgate[2]; // quantization gate/switch
unsigned bank[2] = {0, 0};  // scale banks in use
unsigned scale[2] = {0, 0}; // scales in use

#if DEBUG
unsigned cvold[2] = {9999, 9999}; // previous unquantized CV
unsigned cv2old[2] = {9999, 9999}; // previous transposition CV
unsigned bankold[2] = {9999, 9999}; // previous bank
unsigned scaleold[2] = {9999, 9999}; // previous scale
#endif

// For bank switch there are 6 positions (0 to 5) separated with
// 4 resistors
//
//  GND --0--/\/\/\/--1--/\/\/\/.../\/\/\/--5--VCC
//
// So expect to read values 0, 1023/5, 2*1023/5, ... 1023
//
// or in reality 0 is between 0 and 1023/10, 2 is between
// 1023/10 and 3*1023/10, etc.
// Similarly for scale switch with 12 positions

unsigned bankBins[6] = {102, 307, 512, 716, 921, 1024};
unsigned scaleBins[12] = {47, 140, 233, 326, 419, 512,
			  605, 698, 791, 884, 977, 1024};

void onTrig0RisingEdge();
void onTrig1RisingEdge();

void setup()
{
#if DEBUG
  Serial.begin(9600);
#endif
  dac_inoBoard.begin();
  q[0].SetScale (bank[0], scale[0]);
  q[1].SetScale (bank[1], scale[1]);

  // Set up trigger interrupts
  dac_inoBoard.gateInputInterrupt
    (
     trigChan[0],
     onTrig0RisingEdge,
     dac_ino::GateInterrupt::RisingEdge
     );
  dac_inoBoard.gateInputInterrupt
    (
     trigChan[1],
     onTrig1RisingEdge,
     dac_ino::GateInterrupt::RisingEdge
     );
}

void loop()
{
  // do all this for both quantizers
  
  for (unsigned iq = 0; iq < 2; ++iq)
    {
#if DEBUG
      if (triggered[iq])
	{
	    // There was an interrupt
	    Serial.print ("Oh hey trigger ");
	    Serial.println (iq);
	}
#endif
	  
      // Proceed only IF trigger is on now (which happens if we've
      // input a trigger or if there's nothing plugged into the
      // trigger) or if there's an unhandled interrupt
	  
      if (triggered[iq] || dac_inoBoard.readGate(trigChan[iq]))
	{
	  // Read the rotary switches
	  rsbank[iq] = dac_inoBoard.readCV(bankChan[iq]);
	  rsscale[iq] = dac_inoBoard.readCV(scaleChan[iq]);
	  // Get CV, convert to 12 bits
	  cv[iq] = 4.0 * dac_inoBoard.readCV(cv1InChan[iq]);
	  cv2[iq] = 4.0 * dac_inoBoard.readCV(cv2InChan[iq]);
	  // Check the quantization gate/switch
	  qgate[iq] = dac_inoBoard.readGate(quantInChan[iq]);
	  
	  // Use the rotary switches to determine the banks and scales
      
	  for (unsigned i = 0; i < 6; ++i)
	    if (rsbank[iq] < bankBins[i])
	      {
		rsbank[iq] = i;
		break;
	      }
      
	  for (unsigned i = 0; i < 12; ++i)
	    if (rsscale[iq] < scaleBins[i])
	      {
		rsscale[iq] = i;
		break;
	      }
      
	  if (rsbank[iq] != bank[iq] || rsscale[iq] != scale[iq])
	    {
	      bank[iq] = rsbank[iq];
	      scale[iq] = rsscale[iq];
	      q[iq].SetScale (bank[iq], scale[iq]);
#if DEBUG
	      Serial.print ("Set quantizer "); Serial.print(iq);
	      Serial.print (" bank "); Serial.print (bank[iq]);
	      Serial.print (" scale "); Serial.println (scale[iq]);
#endif
	    }

	  // Quantize the CV but only IF quantize gate is on
	  // which happens if [we've input a gate or there's
	  // nothing plugged into the gate], and [the toggle switch
	  // is on]
	  if (qgate[iq])
	    cvq = q[iq].Quantize(cv[iq]).Value + cv2[iq];
	  else
	    cvq = cv[iq] + cv2[iq];
      
	  // Send it out
	  dac_inoBoard.writeCV(cvOutChan[iq], cvq);
#if DEBUG
	  if (abs(int(cv[iq])-int(cvold[iq])) > 10 || abs(int(cv2[iq])-int(cv2old[iq])) > 10
	  || bank[iq] != bankold[iq] || scale[iq] != scaleold[iq])
	    {
	      Serial.print ("Quantizer "); Serial.print (iq);
	      Serial.print (" CV1 in = "); Serial.print (cv[iq]);
	      Serial.print (" bank "); Serial.print (bank[iq]);
	      Serial.print (" scale "); Serial.print (scale[iq]);
        Serial.print (" quantize "); Serial.print (qgate[iq]);
	      Serial.print (" CV2 in = "); Serial.print (cv2[iq]);
	      Serial.print (" CV out = "); Serial.println (cvq);

	      cvold[iq] = cv[iq];
        cv2old[iq] = cv2[iq];
        bankold[iq] = bank[iq];
        scaleold[iq] = scale[iq];
	    }
#endif
	}
      triggered[iq] = false;
    } // end loop over quantizers
      
  // Take a break, you've earned it
  delayMicroseconds(1000);
}

// When we see a trigger, arrange for quantization ASAP
void onTrig0RisingEdge()
{
  triggered[0] = true;
}

void onTrig1RisingEdge()
{
  triggered[1] = true;
}
