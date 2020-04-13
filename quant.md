# dacarduino dual quantizer

## Inputs (for each section):

Analog:

- CV1, CV2 In:    The CVs to be quantized (mixed; CV2 normalled to +5)
- Scale:          (rotary) Select scale
- Bank:           (rotary) Select bank

Digital:

- Quantize:       Gate to enable quantization, normalled to +5
- Trigger:        Gate to enable sampling, normalled to +5

(Note: if Quantize is off and Trigger is used with short triggers,
this becomes a sample and hold.)

## Outputs (for each section):

Analog:

- CV Out:         Quantized CV


## Scales under consideration

- 12-equal
  - Pentatonic (5)
    - Major (CDEGA)
    - Egyptian (CDFGBb)
    - Blues minor (CEbFAbBb)
    - Blues major (CDFGA)
    - Minor (CEbFGBb)
  - Diatonic (7)
    - Ionian
    - Dorian
    - Phrygian
    - Lydian
    - Mixolydian
    - Aolian
    - Locrian
  - Chromatic (1)
- Just (7)
  - Ionian
  - Dorian
  - Phrygian
  - Lydian
  - Mixolydian
  - Aolian
  - Locrian
- Pythagorean (4)
  - 5 note major
  - 5 note minor
  - 7 note major
  - 7 note minor
  - 12 note
  - 17 note
- Quarter comma (5)
  - 5 note major
  - 5 note minor
  - 7 note major
  - 7 note minor
  - 12 note
  - 19 note
  - 31 note
- Third comma (4)
  - 5 note major
  - 5 note minor
  - 7 note major
  - 7 note minor
  - 12 note
  - 19 note
- 2/7 comma (4)
  - 5 note major
  - 5 note minor
  - 7 note major
  - 7 note minor
  - 12 note
  - 19 note
- Equal divisions
  - First set
    - 1 note (octaves)
    - 2 note (tritones)
    - 3 note (M3)
    - 4 note (m3)
    - 5 note
    - 6 note (whole tones)
    - 7 note
    - 8 note
    - 9 note
    - 10 note
    - 11 note
    - 12 note (semitones)
  - Second set
    - 13 note
    - 14 note
    - 15 note
    - 16 note
    - 17 note
    - 18 note
    - 19 note
    - 20 note
    - 21 note
    - 22 note
    - 23 note
    - 24 note (quarter tones)
- Chords
  - Major triad
  - Minor triad
  - Dominant 7th
  - Major 7th
  - Minor 7th
- Bohlen-Pierce (https://www.ziaspace.com/_academic/BP/page/) (10)
  - Lambda
  - Walker A
  - Moll II
  - Walker I
  - Harmonic
  - Walker II
  - Dur I
  - Moll I
  - Walker B
  - Chromatic

Note on memory usage: Adding scales increases dynamic memory usage a little, because there are longer index arrays, but without PROGMEM usage only the scales actually in use take up more dynamic memory and with it they don't take any to speak of. Program memory usage (for a test of Quantizer library only):

- 2 scales (12-equal and 12-pythagorean) 5616 bytes
- 13 scales (12-equal, 5 pentatonic modes, 7 diatonic modes) 7674 bytes

out of 30720 bytes available. So each scale uses ~ 200 bytes above whatever baseline is used by everything else. If that baseline is ~ 5000 bytes then we have ~ 25000 bytes for scales, enough for about 125 scales. Conveniently close to 12 banks of 12 scales especially if some banks are not filled entirely.

