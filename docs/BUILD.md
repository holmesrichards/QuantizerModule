# Dual Quantizer Build Notes

## dac/ino build information
Current version uses v1.3 release of the [dac/ino](https://github.com/holmesrichards/dac_ino) board. See that repository for general building information.

Dual Quantizer does not use:

* Gate Out A and B
* All pin headers (aside from 3-pin jumper headers)
* VCC/Gnd Molex header

so these components can be omitted: Q1, Q2, R10–13 (don't omit R14!), J5–J8, J10, J11, J14

dac/ino CV outputs can range 0–10V or ±5V. Set jumpers for 0–10V outputs. Since CV1 is limited to 0–5V, the quantized CV1 will also be limited to about 0–5V, but the CV2 offset can change the output range up to 5–10V. If desired you can omit J1 and J2 in favor of hardwired jumpers.

Use 35 mm spacers to mount dac/ino board to the panel after wiring is done.

## Quantizer panel

Mount panel components to the panel, then wire (referring to [panel components schematic](docs/quantpc.pdf)):

* CV1 In tip normal pins to sleeve pins. Connect sleeve and tip pins to 2-pin Molex connectors to CV In A and C on the dac/ino board (ground is on the right side of the Molex connector as viewed from the tab side).
* CV2 In tip pins to pin 3 on the attenuators. Connect sleeves to ground. 
* Quantize tip to bottom terminals of toggle switches. Connect sleeves to ground. 
* Trigger tips and sleeves to Molex connectors to Gate In A and B.
* CV Out tips to Molex connectors to CV Out A and B.
* Resistors to CV2, Quantize, and Gate tip normal pins. Other ends of resistors to VCC pin on 8 pin Molex connector.
* Resistors to toggle middle terminals. Middle terminal (ground) and resistor to 2-pin Molex to Gate In C and D.
* Attenuator pins 1 and 2 to a 2-pin Molex connector (pin 1 is ground) to CV In B and D.
* On Scale rotary switches, add 11 resistors between the 12 pins. Wire center pin to 8 pin Molex as shown in circuit diagram. Connect pin 1 to ground and 12 to VCC from 8 pin Molex. Do the same for the Bank switches but only pins 1 through 6. Here's a photo:  
<img src="rotswitch.jpg" width=640>

Wiring photo:  
<img src="quantizer_back.jpg" width=320>

BOM for the panel components is [here](quantpc_bom.md).
