# QuantizerModule
Code and hardware for Kosmo/Eurorack quantizer module

This is a dual quantizer based on the [dacarduino](https://github.com/holmesrichards/dacarduino) board. As such it uses the dacarduino library as well as the Quantizer library in this repository.

Design is for Kosmo format module but the PCB and code would work equally well for a Eurorack version. It would just need a smaller front panel.

THIS IS A WORK IN PROGRESS.

The eventual intention is to have on the front panel, for each quantizer section:

- CV input, maybe two inputs one with attenuator to be mixed.
- Quantize gate input. If a gate source is plugged in here, quantization happens only when the gate is on. Otherwise the unquantized input is fed to the output. If no gate source is plugged in, quantization is always on. Except:
- Toggle switch. If in the off position, no quantization occurs.
- Trigger input. If a trigger source is plugged in here, the input CV is sampled and the output CV changed only when there is a trigger. Otherwise the output CV is held. If no trigger source is plugged in, the input CV is sampled and the output CV changed "continuously" (i.e. at some rapid rate). This gives a quantized (or not) sample and hold functionality.
- CV output.
- Scale selector. 12 position switch.
- Bank selector. 12 position switch.

There can be up to 12 scales stored in each of up to 12 banks, which makes 144 scales for those of you who've lost your calculator. ("Up to." Depending on the scales, 144 of them might exceed the Arduino's program memory capacity.) The scales are defined in the code and it's easy enough to change. There's a mechanism to convert Scala format scale files into data for the Quantizer library.