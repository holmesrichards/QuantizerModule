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

- Bank 1 [0 array index]: Top twelve (all based on 12-equal)
  1. Chromatic
  2. Major C D E F G A B 
  3. Natural minor C D Eb F G Ab Bb 
  4. Harmonic minor C D Eb F G Ab B 
  5. Major pentatonic C D E G A
  6. Minor pentatonic C Eb F G Bb
  7. Hexatonic blues C Eb F F# G Bb 
  8. Whole tone C D E F# G# A#
  9. Major triad C E G
  10. Minor triad C Eb G
  11. Dominant seventh C E G Bb
  12. Diminished seventh C Eb Gb A

- Bank 2: Modes (all based on 12-equal)
  - Pentatonic
    1. Major (CDEGA)
    2. Egyptian (CDFGBb)
    3. Blues minor (CEbFAbBb)
    4. Blues major (CDFGA)
    5. Minor (CEbFGBb)
  - Diatonic
    6. Ionian
    - Dorian
    - Phrygian
    - Lydian
    - Mixolydian
    - Aolian
    - Locrian
	
- Bank 3: Just intonation/Pythagorean
  - Just intonation
    1. Ptolemy's Intense Diatonic Syntonon, also Zarlino's scale (scl/ptolemy.scl)
    2. Ellis's Duodene : genus [33355] (scl/duodene.scl)
    3. 5-limit diamond 1/1 6/5 5/4 4/3 3/2 8/5 5/3
    4. 7-limit diamond 1/1 8/7 7/6 6/5 5/4 4/3 7/5 10/7 3/2 8/5 5/3 12/7 7/4
    5. Harry Partch's 43-tone pure scale (scl/partch_43.scl)
    6. reserved
    6. reserved
    6. reserved
  - Pythagorean all g 3/2 p 2/1
    9. 5 note 
    - 7 note 
    - 12 note
    - 17 note

- Bank 4: Meantone
  - Quarter comma all g 3/2-.25 comma
    1. 5 note
    - 7 note
    - 12 note
    - 19 note
    - 31 note
  - Third comma all g 3/2-.33 comma
    1. 5 note
    - 7 note
    - 12 note
    - 19 note
  - 2/7 comma all g 3/2-.28 comma
     1. 5 note
     - 7 note
     - 12 note
	
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

