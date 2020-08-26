# dac/ino dual quantizer

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


## Banks and scales (as provided, but can be reprogrammed)

- Bank 1 [0 array index]: Top twelve. (Note a few of these duplicate later entries. However only the index is duplicated; the scales themselves are stored only once.)
  1. Chromatic C C# D Eb E F F# G G# A Bb B
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

- Bank 2: Just intonation/Pythagorean
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

- Bank 3: Meantone
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
 
- Bank 4: Well temperaments
  1. Werckmeister III
  - Werckmeister IV
  - Werckmeister V
  - Werckmeister VI
  - Neidhardt I
  - Neidhardt II
  - Neidhardt III
  - Kirnberger II
  - Kirnberger III
  - Vallotti
  - Young 1
  - Young 2

- Bank 5: Macrotonal (and 12-note) equal divisions
  1. 1 note (octaves)
  - 2 note (tritones)
  - 3 note (major thirds)
  - 4 note (minor thirds or diminished seventh)
  - 5 note
  - 6 note (whole tones)
  - 7 note
  - 8 note
  - 9 note
  - 10 note
  - 11 note
  - 12 note (semitones)

- Bank 6: Microtonal equal divisions
  1. 13 note
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

In principle the code can be modified to handle more banks, but the chosen scales just about fill the program memory on the Nano.
