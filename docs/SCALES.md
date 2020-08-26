# Dual Quantizer scales

There are two sets of scales provided in the software. The "Common Scales" set is enabled by default. Change the value of SCALESET in Quantize.h to get the "Esoteric Scales" set. To customize the scales see [change scale instructions](CHANGESCALES.md).

## Common Scales set
<ul>
<li>Bank 1 [0 array index]: Top twelve. (Note a few of these duplicate later entries. However, only the index is duplicated; the scales themselves are stored only once.)
<ol type="1">
<li>Chromatic: C C# D Eb E F F# G G# A Bb B</li>
<li>Major: C D E F G A B </li>
<li>Natural minor: C D Eb F G Ab Bb </li>
<li>Harmonic minor: C D Eb F G Ab B </li>
<li>Major pentatonic: C D E G A</li>
<li>Minor pentatonic: C Eb F G Bb</li>
<li>Hexatonic blues: C Eb F F# G Bb </li>
<li>Whole tone: C D E F# G# A#</li>
<li>Major triad: C E G</li>
<li>Minor triad: C Eb G</li>
<li>Dominant seventh: C E G Bb</li>
<li>Diminished seventh: C Eb Gb A</li>
</ol>
</li><br>
<li> Bank 2: Diatonic (major/natural minor) scales
<ol type="1">
<li>C  major / A  natural minor: C D E F G A B </li>
<li>C# major / Bb natural minor</li>
<li>D  major / B  natural minor</li>
<li>Eb major / C  natural minor</li>
<li>E  major / C# natural minor</li>
<li>F  major / D  natural minor</li>
<li>F# major / Eb natural minor</li>
<li>G  major / E  natural minor</li>
<li>G# major / F  natural minor</li>
<li>A  major / F# natural minor</li>
<li>Bb major / G  natural minor</li>
<li>B  major / G# natural minor</li>
</ol>
</li><br>
<li> Bank 3: Harmonic minor scales
<ol type="1">
<li>C  harmonic minor: C D Eb F G Ab B </li>
<li>C# harmonic minor</li>
<li>D  harmonic minor  </li>
</ol>
and so on
</li><br>
<li> Bank 4: Melodic minor (ascending/jazz) scales
<ol type="1">
<li>C  melodic minor: C D Eb F G A B </li>
<li>C# melodic minor</li>
<li>D  melodic minor  </li>
</ol>
  and so on
</li><br>
<li> Bank 5: Pentatonic scales
<ol type="1">
<li>C  major / A minor pentatonic: C D E G A</li>
<li>C# major / Bb minor pentatonic</li>
<li>D  major / B minor pentatonic  </li>
</ol>
  and so on
</li><br>
<li> Bank 6: Hexatonic blues scales
<ol type="1">
<li>C  blues: C Eb F F# G Bb </li>
<li>C# blues</li>
<li>D  blues  </li>
</ol>
and so on
</li>
</ul>

## Esoteric Scales set
<ul>
	<li>Bank 1: Same as Common Scales Bank 1
	</li><br>
	<li> Bank 2: Just intonation/Pythagorean
	<ol type=1>
		<li>Ptolemy's Intense Diatonic Syntonon, also Zarlino's scale (scl/ptolemy.scl)</li>
		<li>Ellis's Duodene : genus [33355] (scl/duodene.scl)</li>
		<li>5-limit diamond 1/1 6/5 5/4 4/3 3/2 8/5 5/3</li>
		<li>7-limit diamond 1/1 8/7 7/6 6/5 5/4 4/3 7/5 10/7 3/2 8/5 5/3 12/7 7/4</li>
		<li>Harry Partch's 43-tone pure scale (scl/partch_43.scl)</li>
		<li>reserved</li>
		<li>reserved</li>
		<li>reserved</li>
		<li>Pythagorean 5 note </li>
		<li>Pythagorean 7 note </li>
		<li>Pythagorean 12 note</li>
		<li>Pythagorean 17 note</li>
	</ol>
	</li><br>
	<li> Bank 3: Meantone
	<ol type=1>
		<li>Quarter comma 5 note</li>
		<li>Quarter comma 7 note</li>
		<li>Quarter comma 12 note</li>
		<li>Quarter comma 19 note</li>
		<li>Third comma 5 note</li>
		<li>Third comma 7 note</li>
		<li>Third comma 12 note</li>
		<li>Third comma 19 note</li>
		<li>2/7 comma 5 note</li>
		<li>2/7 comma 7 note</li>
		<li>2/7 comma 12 note</li>
	</ol>
	</li><br>
	<li> Bank 4: Well temperaments
	<ol type="1">
		<li>Werckmeister III</li>
		<li>Werckmeister IV</li>
		<li>Werckmeister V</li>
		<li>Werckmeister VI</li>
		<li>Neidhardt I</li>
		<li>Neidhardt II</li>
		<li>Neidhardt III</li>
		<li>Kirnberger II</li>
		<li>Kirnberger III</li>
		<li>Vallotti</li>
		<li>Young 1</li>
		<li>Young 2</li>
	</ol>
	</li><br>
	<li> Bank 5: Macrotonal (and 12-note) equal divisions
	<ol type="1">
		<li>1 note (octaves)</li>
		<li>2 note (tritones)</li>
		<li>3 note (major thirds)</li>
		<li>4 note (minor thirds or diminished seventh)</li>
		<li>5 note</li>
		<li>6 note (whole tones)</li>
		<li>7 note</li>
		<li>8 note</li>
		<li>9 note</li>
		<li>10 note</li>
		<li>11 note</li>
		<li>12 note (semitones)</li>
	</ol>
	</li><br>
	<li> Bank 6: Microtonal equal divisions
	<ol type="1">
		<li>13 note</li>
		<li>14 note</li>
		<li>15 note</li>
		<li>16 note</li>
		<li>17 note</li>
		<li>18 note</li>
		<li>19 note</li>
		<li>20 note</li>
		<li>21 note</li>
		<li>22 note</li>
		<li>23 note</li>
		<li>24 note (quarter tones)</li>
	</ol>
	</li><br>
</ul>
