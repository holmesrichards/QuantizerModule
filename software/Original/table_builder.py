#!/usr/bin/python

import sys, getopt, math



def readFile(inputfile, scalenum, outputhandle, notecounter):

	description = ""
	values = 0
	scale = []


	with open(inputfile) as f:
	    for line in f:
			line = line.strip()

			# if it is a comment - skip it
			if line.startswith("!"):
				continue

			if description == "":
				description = line
			elif values == 0:
				values = line
			elif "/" in line:
				ratio = line.split("/")
				value = float(ratio[0]) / float(ratio[1])
				value = math.log(value) * 1200 / math.log(2)
				scale.append(value)
			else:
				scale.append(float(line))


	table = []
	freqs = []

	# assume that 0v is C0 and loop over the scale until we have exceeded 16384
	centstoint = 16383. / 10. / 1200.
	cents = 0.
	note = 0
	octave = 0

	table.append(cents)
	freq = 16.351597831287414 * math.pow(2, ((cents / 1638.3) - 1.))
	freqs.append(freq)

	while cents <= 16384.:
		cents = (scale[note] * centstoint) + octave
		table.append(cents)
		freq = 16.351597831287414 * math.pow(2, ((cents / 1638.3) - 1.))
		freqs.append(freq)
		note += 1
		if note >= len(scale):
			octave = cents
			note = 0

	pitchCount = len(table)
	notecounter.append(pitchCount)

	# generate volt octave hints
	octave = 0
	tovoltoctave = 16383. / 10.
	hints = [ 0 ]
	i = 0
	for note in table:
		if (int(float(note) / tovoltoctave) > octave):
			hints.append(i)
			octave += 1
		i += 1

	# stringify

	table = ','.join(map(str, table)) 
	freqs = ','.join(map(str, freqs)) 
	hints = ','.join(map(str, hints)) 


	outputhandle.write("// " + inputfile + "\n")
	outputhandle.write("// " + description + "\n")
	outputhandle.write("const float Quantizer::scale" + str(scalenum) + "[] = { " + table + " };" + "\n")
	outputhandle.write("const float Quantizer::freqs" + str(scalenum) + "[] = { " + freqs + " };" + "\n")
	outputhandle.write("const int Quantizer::hints" + str(scalenum) + "[] = { " + hints + " };" + "\n")


# MAIN

argv = sys.argv[1:]

try:
  opts, args = getopt.getopt(argv,"i::",["input="])
except getopt.GetoptError:
  print "table_builder.py -i <inputfile>"
  sys.exit(2)

inputfile = ""

notecounter = []

for opt, arg in opts:
  if opt in ("-i", "--ifile"):
     inputfile = arg

if inputfile == "":
	sys.exit(2)

i = 0

scales = []
hints = []
freqs = []

with open("scales.cpp", "w") as outputfile:
	with open(inputfile) as list:
	    for item in list:
			item = item.strip()
			readFile(item, i, outputfile, notecounter)
			scales.append('scale' + str(i))
			freqs.append('freqs' + str(i))
			hints.append('hints' + str(i))
			i += 1

	notelist = ','.join(map(str, notecounter))
	scales = ','.join(map(str, scales))
	freqs = ','.join(map(str, freqs))
	hints = ','.join(map(str, hints))

	outputfile.write("\n");
	outputfile.write("const int Quantizer::notecount[] = { " + notelist + " };" + "\n")
	outputfile.write("\n");

	outputfile.write("const float *Quantizer::scales[] = { " + scales + " };" + "\n")
	outputfile.write("const float *Quantizer::freqs[] = { " + freqs + " };" + "\n")
	outputfile.write("const int *Quantizer::hints[] = { " + hints + " };" + "\n")

	outputfile.write("\n\n");
	outputfile.write("// for protected header\n");
	outputfile.write("const static int scaleCount = " + str(i) + ";\n");
	outputfile.write("static const int *hints[" + str(i) + "];\n");
	outputfile.write("static const float *scales[" + str(i) + "];\n");
	outputfile.write("static const float *freqs[" + str(i) + "];\n");
	outputfile.write("static const int notecount[" + str(i) + "];\n");
	outputfile.write("\n");

	i = 0

	for notecount in notecounter:
		outputfile.write("static const float scale" + str(i) + "[" + str(notecount) + "];\n");
		outputfile.write("static const float freqs" + str(i) + "[" + str(notecount) + "];\n");
		outputfile.write("static const int hints" + str(i) + "[" + str(notecount) + "];\n");
		i += 1;


