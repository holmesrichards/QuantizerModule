# Dual Quantizer scales

There are two sets of scales provided in the software. The "Common Scales" set is enabled by default. Change the value of SCALESET in Quantize.h to get the "Esoteric Scales" set. To customize the scales see [change scale instructions](CHANGESCALES.md).

## Common Scales set
- Bank 1 [0 array index]: Top twelve. (Note a few of these duplicate later entries. However, only the index is duplicated; the scales themselves are stored only once.)
  1. Chromatic: C C# D Eb E F F# G G# A Bb B
  2. Major: C D E F G A B 
  3. Natural minor: C D Eb F G Ab Bb 
  4. Harmonic minor: C D Eb F G Ab B 
  5. Major pentatonic: C D E G A
  6. Minor pentatonic: C Eb F G Bb
  7. Hexatonic blues: C Eb F F# G Bb 
  8. Whole tone: C D E F# G# A#
  9. Major triad: C E G
  10. Minor triad: C Eb G
  11. Dominant seventh: C E G Bb
  12. Diminished seventh: C Eb Gb A
  
- Bank 2: Diatonic (major/natural minor) scales
  1. C  major / A  natural minor: C D E F G A B 
  2. C# major / Bb natural minor
  3. D  major / B  natural minor
  4. Eb major / C  natural minor
  5. E  major / C# natural minor
  6. F  major / D  natural minor
  7. F# major / Eb natural minor
  8. G  major / E  natural minor
  9. G# major / F  natural minor
  10. A  major / F# natural minor
  11. Bb major / G  natural minor
  12. B  major / G# natural minor
  
- Bank 3: Harmonic minor scales
  1. C  harmonic minor: C D Eb F G Ab B 
  2. C# harmonic minor
  3. D  harmonic minor  
 and so on
  
- Bank 4: Melodic minor (ascending/jazz) scales
  1. C  melodic minor: C D Eb F G A B 
  2. C# melodic minor
  3. D  melodic minor  
  and so on
  
- Bank 5: Pentatonic scales
  1. C  major / A minor pentatonic: C D E G A
  2. C# major / Bb minor pentatonic
  3. D  major / B minor pentatonic  
  and so on
  
- Bank 6: Hexatonic blues scales
  1. C  blues: C Eb F F# G Bb 
  2. C# blues
  3. D  blues  
and so on

## Esoteric Scales set
- Bank 1: Same as Common Scales Bank 1

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
  - Pythagorean
    9. 5 note 
    - 7 note 
    - 12 note
    - 17 note

- Bank 3: Meantone
  - Quarter comma
    1. 5 note
    - 7 note
    - 12 note
    - 19 note
    - 31 note
  - Third comma
    1. 5 note
    - 7 note
    - 12 note
    - 19 note
  - 2/7 comma
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
