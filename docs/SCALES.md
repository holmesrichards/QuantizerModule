# Dual Quantizer scales

There are two sets of scales provided in the software. The "Common Scales" set is enabled by default. Change the value of SCALESET in Quantize.h to get the "Esoteric Scales" set. To customize the scales see [change scale instructions](CHANGESCALES.md).

## Common Scales set
* Bank 1 [0 array index]: Top twelve. (Note a few of these duplicate later entries. However, only the index is duplicated; the scales themselves are stored only once.)
  1. Chromatic: C C# D Eb E F F# G G# A Bb B
  1. Major: C D E F G A B 
  1. Natural minor: C D Eb F G Ab Bb 
  1. Harmonic minor: C D Eb F G Ab B 
  1. Major pentatonic: C D E G A
  1. Minor pentatonic: C Eb F G Bb
  1. Hexatonic blues: C Eb F F# G Bb 
  1. Whole tone: C D E F# G# A#
  1. Major triad: C E G
  1. Minor triad: C Eb G
  1. Dominant seventh: C E G Bb
  1. Diminished seventh: C Eb Gb A

* Bank 2: Diatonic (major/natural minor) scales
  1. C  major / A  natural minor: C D E F G A B 
  1. C# major / Bb natural minor
  1. D  major / B  natural minor
  1. Eb major / C  natural minor
  1. E  major / C# natural minor
  1. F  major / D  natural minor
  1. F# major / Eb natural minor
  1. G  major / E  natural minor
  1. G# major / F  natural minor
  1. A  major / F# natural minor
  1. Bb major / G  natural minor
  1. B  major / G# natural minor

* Bank 3: Harmonic minor scales
  1. C  harmonic minor: C D Eb F G Ab B 
  1. C# harmonic minor
  1. D  harmonic minor  
and so on

* Bank 4: Melodic minor (ascending/jazz) scales
  1. C  melodic minor: C D Eb F G A B 
  1. C# melodic minor
  1. D  melodic minor  
  and so on

* Bank 5: Pentatonic scales
  1. C  major / A minor pentatonic: C D E G A
  1. C# major / Bb minor pentatonic
  1. D  major / B minor pentatonic  
  and so on

* Bank 6: Hexatonic blues scales
  1. C  blues: C Eb F F# G Bb 
  1. C# blues
  1. D  blues  
and so on

</ul>

## Esoteric Scales set
* Bank 1: Same as Common Scales Bank 1
* Bank 2: Just intonation/Pythagorean
   1. Ptolemy's Intense Diatonic Syntonon, also Zarlino's scale (scl/ptolemy.scl)
   1. Ellis's Duodene : genus [33355] (scl/duodene.scl)
   1. 5-limit diamond 1/1 6/5 5/4 4/3 3/2 8/5 5/3
   1. 7-limit diamond 1/1 8/7 7/6 6/5 5/4 4/3 7/5 10/7 3/2 8/5 5/3 12/7 7/4
   1. Harry Partch's 43-tone pure scale (scl/partch_43.scl)
   1. reserved
   1. reserved
   1. reserved
   1. Pythagorean 5 note 
   1. Pythagorean 7 note 
   1. Pythagorean 12 note
   1. Pythagorean 17 note

* Bank 3: Meantone
  1. Quarter comma 5 note
  1. Quarter comma 7 note
  1. Quarter comma 12 note
  1. Quarter comma 19 note
  1. Quarter comma 31 note
  1. Third comma 5 note
  1. Third comma 7 note
  1. Third comma 12 note
  1. Third comma 19 note
  1. 2/7 comma 5 note
  1. 2/7 comma 7 note
  1. 2/7 comma 12 note

* Bank 4: Well temperaments
  1. Werckmeister III
  1. Werckmeister IV
  1. Werckmeister V
  1. Werckmeister VI
  1. Neidhardt I
  1. Neidhardt II
  1. Neidhardt III
  1. Kirnberger II
  1. Kirnberger III
  1. Vallotti
  1. Young 1
  1. Young 2

* Bank 5: Macrotonal (and 12-note) equal divisions
  1. 1 note (octaves)
  1. 2 note (tritones)
  1. 3 note (major thirds)
  1. 4 note (minor thirds or diminished seventh)
  1. 5 note
  1. 6 note (whole tones)
  1. 7 note
  1. 8 note
  1. 9 note
  1. 10 note
  1. 11 note
  1. 12 note (semitones)

* Bank 6: Microtonal equal divisions
  1. 13 note
  1. 14 note
  1. 15 note
  1. 16 note
  1. 17 note
  1. 18 note
  1. 19 note
  1. 20 note
  1. 21 note
  1. 22 note
  1. 23 note
  1. 24 note (quarter tones)

