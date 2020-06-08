# QuantizerModule
Code and hardware for Kosmo/Eurorack quantizer module

This is a dual quantizer based on the [dac/ino](https://github.com/holmesrichards/dac_ino) board. As such it uses the dac_ino library as well as the Quantizer library in this repository.

Design is for Kosmo format module but the PCB and code would work equally well for a Eurorack version if the board were mounted perpendicular to the panel. It would just need a smaller front panel. Likewise with perpendicular mounting it could be a smaller single Kosmo quantizer.

THIS IS A WORK IN PROGRESS.

The eventual intention is to have on the front panel, for each quantizer section:

- CV input, maybe two inputs one with attenuator to be mixed.
- Quantize gate input. If a gate source is plugged in here, quantization happens only when the gate is on. Otherwise the unquantized input is fed to the output. If no gate source is plugged in, quantization is always on. Except:
- Toggle switch. If in the off position, no quantization occurs.
- Trigger input. If a trigger source is plugged in here, the input CV is sampled and the output CV changed only when there is a trigger. Otherwise the output CV is held. If no trigger source is plugged in, the input CV is sampled and the output CV changed "continuously" (i.e. at some rapid rate). This gives a quantized (or not) sample and hold functionality.
- CV output.
- Scale selector. 12 position switch.
- Bank selector. 6 position switch.

There can be up to 12 scales stored in each of up to 6 banks, which makes 72 scales for those of you who've lost your calculator. ("Up to." Depending on the scales, 72 of them might exceed the Arduino's program memory capacity.) 65 scales are defined in the code and it's easy enough to change them. There's a mechanism to convert Scala format scale files, or definitions in terms of equal divisions of the octave or generators and periods into data for the Quantizer library.

Current version uses v1.2 release of dac/ino. (Note that current version of dac/ino is incompatible due to rearrangement of headers.) It does not use either Gate Out A or B, nor does it use the Molex headers for CV In B and D, so these can be omitted from the dac/ino assembly.
