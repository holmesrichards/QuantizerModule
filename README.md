# QuantizerModule
Code and hardware for Kosmo/Eurorack quantizer module

This is a dual quantizer based on the [dac/ino](https://github.com/holmesrichards/dac_ino) board. As such it uses the dac_ino library as well as the Quantizer library in this repository.

Design is for Kosmo format module but the PCB and code would work equally well for a Eurorack version if the board were mounted perpendicular to the panel. It would just need a smaller front panel. Likewise with perpendicular mounting it could be a smaller single Kosmo quantizer.

## Front panel
On the front panel, for each quantizer section, are:

- CV1 and CV2 inputs
- Quantize gate input
- Trigger input
- CV output
- CV2 attenuator
- Quantize toggle switch
- Scale selection 12 position rotary switch
- Bank selection 6 position switch

## Use
The control voltage to be quantized is plugged into CV1. It should be in the range 0–5 volts, though voltages outside this range (within reason) shouldn't cause damage.

CV2 is an offset; it is added to the quantized CV1 to produce the output. It should also be in the range 0–5 volts. It can be attenuated with the knob. Normalled value is 5 volts before attenuation.

The Quantize switch can be used to disable quantization, in which case the output CV is just CV1 + CV2 (attenuated). If the Quantize switch is on and a gate source is plugged into the Quantize input, quantization is on only when the gate is on. If nothing is plugged in and the Quantize switch is on, quantization is on.

If nothing is plugged into the Trigger input, the input control voltages are sampled and the output control voltage is updated continually. If a trigger or gate source is plugged in, updating occurs only when a trigger or gate is present. In that case the module behaves like a quantizing (or not, if quantizing is off) sample and hold.

The rotary switches are used to select a bank of scales and a scale within that bank. There can be up to 12 scales stored in each of up to 6 banks, which makes 72 scales for those of you who've lost your calculator. ("Up to." Depending on the scales, 72 of them might exceed the Arduino's program memory capacity.) See [scales document](./docs/SCALES.md) for the scales built into the software as supplied. If you want other scales it's easy enough to change them. There's a mechanism to convert Scala format scale files, or definitions in terms of equal divisions of the octave or generators and periods into data for the Quantizer library. See [change scale instructions](./docs/CHANGESCALES.md).

## dac/ino build information
Current version uses v1.3 release of the dac/ino board. 

Quantizer does not use:

* Gate Out A and B
* All pin headers (aside from 3-pin jumper headers)
* VCC/Gnd Molex header

so these components can be omitted: Q1, Q2, R10–13 (don't omit R14!), J5–J8, J10, J11, J14

dac/ino CV outputs can range 0–10V or ±5V. Set jumpers for 0–10V outputs. Since CV1 is limited to 0–5V, the quantized CV1 will also be limited to about 0–5V, but the CV2 offset can change the output range up to 0–10V. If desired you can omit J1 and J2 in favor of hardwired jumpers.

Use 35 mm spacers to mount dac/ino board to the panel after wiring is done.

Mount panel components to the panel, then wire (referring to [panel components schematic](docs/quantpc.pdf):

* CV1 In tip normal pins to sleeve pins. Connect sleeve and tip pins to 2-pin Molex connectors to CV In A and C on the dac/ino board (ground is on the right side of the Molex connector as viewed from the tab side).
* CV2 In tip pins to pin 3 on the attenuators. Connect sleeves to ground. 
* Quantize tip to bottom terminals of toggle switches. Connect sleeves to ground. 
* Trigger tips and sleeves to Molex connectors to Gate In A and B.
* CV Out tips to Molex connectors to CV Out A and B.
* Resistors to CV2, Quantize, and Gate tip normal pins. Other ends of resistors to VCC pin on 8 pin Molex connector.
* Resistors to toggle middle terminals. Middle terminal (ground) and resistor to 2-pin Molex to Gate In C and D.
* Attenuator pins 1 and 2 to a 2-pin Molex connector (pin 1 is ground) to CV In B and D.
* On Scale rotary switches, add 11 resistors between the 12 pins. Wire center pin to 8 pin Molex as shown in circuit diagram. Connect pin 1 to ground and 12 to VCC from 8 pin Molex. Do the same for the Bank switches but only pins 1 through 6.
