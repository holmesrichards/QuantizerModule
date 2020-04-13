/*

Dual Quantizer
Rich Holmes 4/2020

Uses dacarduino library to communicate with board and quantize library
to do the quantization, this is just the glue in between...

 */

#include <dacarduino.h>
#include <Quantizer.h>

//  0 - 4095  = 0 - 5V
//  0 - 819   = 0 - 1V
//  68.25 = 1V / 12

#define OCTAVE (4095 / 5)
#define NOTE (OCTAVE / 12)
#define DEBUG true

using namespace dcrd;

Quantizer q[2];

dacarduino::CVChannel cvchan[2] = {dacarduino::CVChannel::A, dacarduino::CVChannel::B};
dacarduino::CVChannel psbankchan[2] = {dacarduino::CVChannel::C, dacarduino::CVChannel::E};
dacarduino::CVChannel psscalechan[2] = {dacarduino::CVChannel::D, dacarduino::CVChannel::F};
dacarduino::GateChannel gatechan[2] = {dacarduino::GateChannel::A, dacarduino::GateChannel::C};
dacarduino::GateChannel trigchan[2] = {dacarduino::GateChannel::B, dacarduino::GateChannel::D};

int cv; // the CV before and after quantization
int ps[2]; // position switch states
int bank[2] = {0, 0};  // scale banks in use
int scale[2] = {0, 0}; // scales in use

#if DEBUG
// Trigger diagnostics
bool triggered[2] = {false, false};
int cvtrig[2] = {-1, -1};
#endif

void onGateARisingEdge();
void onGateBRisingEdge();

void setup()
{
#if DEBUG
  Serial.begin(9600);
#endif
  dacarduinoBoard.begin();
  q[0].SetScale (bank[0], scale[0]);
  q[1].SetScale (bank[1], scale[1]);

  // Set up trigger interrupts
  dacarduinoBoard.gateInputInterrupt
    (
     trigchan[0],
     onTrig0RisingEdge,
     dacarduino::GateInterrupt::RisingEdge
     );
  dacarduinoBoard.gateInputInterrupt
    (
     trigchan[1],
     onTrig1RisingEdge,
     dacarduino::GateInterrupt::RisingEdge
     );
}

void loop()
{
  // do all this for both quantizers
  
  for (int iq = 0; iq < 2; ++iq)
    {
      // Read the rotary switches
      ps[0] = dacarduinoBoard.readCV(psbankchan[iq]);
      ps[1] = dacarduinoBoard.readCV(psscalechan[iq]);
      
#if DEBUG
      if (triggered[iq])
	{
	  Serial.print ("Oh hey trigger ");
	  Serial.print (iq);
	  Serial.print (" CV = ");
	  Serial.println (cvtrig[iq]);
	  triggered[iq] = false;
	  cvtrig[iq] = -1;
	}
      Serial.print ("Read quantizer ");
      Serial.print (iq);
      Serial.print (" bank switch = ");
      Serial.print (ps[0]);
      Serial.print (" scale switch = ");
      Serial.println (ps[1]);
#endif

      // Use the rotary switches to determine the banks and scales
      
      // There are 12 positions (0 to 11) separated with 11 resistors
      //
      //  GND --0--/\/\/\/--1--/\/\/\/.../\/\/\/--11--VCC
      //
      // So expect to read values 0, 1023/11, 2*1023/11, ... 1023
      //
      // or in reality 0 is between 0 and 1023/22, 2 is between
      // 1023/22 and 3*1023/22, etc.
      
      for (int i = 0; i < 2; ++i)
	{
	  if (ps[i] > 977)
	    ps[i] = 11;
	  else if (ps[i] > 884)
	    ps[i] = 10;
	  else if (ps[i] > 791)
	    ps[i] = 9;
	  else if (ps[i] > 698)
	    ps[i] = 8;
	  else if (ps[i] > 605)
	    ps[i] = 7;
	  else if (ps[i] > 512)
	    ps[i] = 6;
	  else if (ps[i] > 419)
	    ps[i] = 5;
	  else if (ps[i] > 326)
	    ps[i] = 4;
	  else if (ps[i] > 233)
	    ps[i] = 3;
	  else if (ps[i] > 140)
	    ps[i] = 2;
	  else if (ps[i] > 47)
	    ps[i] = 1;
	  else
	    ps[i] = 0;
	}
      if (ps[0] != bank[iq] || ps[1] != scale[iq])
	{
	  bank[iq] = ps[0];
	  scale[iq] = ps[1];
	  q[iq].SetScale (bank[iq], scale[iq]);
#if DEBUG
	  Serial.print ("Set bank ");
	  Serial.print (bank[iq]);
	  Serial.print (" scale ");
	  Serial.println (scale[iq]);
#endif
	}

      // Handle CV but only IF trigger is on
      // which happens if we've input a trigger or if there's
      // nothing plugged into the trigger
      bool trig = dacarduinoBoard.readGate(trigchan[iq]);
      if (trig)
	{
	  cv = dacarduinoBoard.readCV(cvchan[iq]);

#if DEBUG
	  Serial.print ("Read quantizer ");
	  Serial.print (iq);
	  Serial.print (" CV = ");
	  Serial.println (cv);
#endif      
	  // Quantize the CV but only IF gate is on
	  // which happens if we've input a gate or if there's
	  // nothing plugged into the gate, and the toggle switch
	  // is on
	  bool gate = dacarduinoBoard.readGate(gatechan[iq]);
	  if (gate)
	    cv = q[iq].Quantize(cv).Value;
      
	  // Send it out
	  dacarduinoBoard.writeCV(cvchan[iq], cv);
#if DEBUG
	  Serial.print ("Set CV ");
	  Serial.println (cv);
#endif
	}
    } // end loop over quantizers
  
  // Take a break, you've earned it
#if DEBUG
  delay(1000);
#endif
  delayMicroseconds(100);
}

// When we see a trigger, quantize the input immediately
void onTrig0RisingEdge()
{
  cv = dacarduinoBoard.readCV(cvchan[0]);
  cv = q[0].Quantize(cv).Value;
  dacarduinoBoard.writeCV(cvchan[0], cv);
#if DEBUG
  cvtrig[0] = cv;
  triggered[0] = true;
#endif
}

void onTrig1RisingEdge()
{
  cv = dacarduinoBoard.readCV(cvchan[1]);
  cv = q[1].Quantize(cv).Value;
  dacarduinoBoard.writeCV(cvchan[1], cv);
#if DEBUG
  cvtrig[0] = cv;
  triggered[0] = true;
#endif
}

