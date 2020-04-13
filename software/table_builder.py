#!/usr/bin/python

# * Quantizer
# * Rich Holmes
# * 
# * Based on:
# * table_builder.py from https://github.com/bpcmusic/telex_scales
#
# * Removed frequency table, added PROGMEM to declarations

import sys, getopt, math

DACTOP = 4095   # limit of DAC (2**12-1)
DAC1   = 4095   # DAC counts corresponding to defined voltage
V1     = 5.0    # voltage corresponding to DAC1
DACPEROCTAVE  = (DAC1/V1)  # DAC counts per octave

def readFile(inputfile, scalenum, outputhandle, notecounter):
    description = ""
    values = 0
    scale = []

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

    # assume that 0v is C0 and loop over the scale until we have exceeded DACTOP
    centstodac = DACPEROCTAVE / 1200.
    dacs = 0.
    note = 0
    octave = 0

    table.append(dacs)

    while dacs <= DACTOP:
	dacs = (scale[note] * centstodac) + octave
	table.append(dacs)
	note += 1
	if note >= len(scale):
	    octave = dacs
	    note = 0

    pitchCount = len(table)
    notecounter.append(pitchCount)

    # generate volt octave hints
    octave = 0
    hints = [ 0 ]
    i = 0
    for note in table:
	if (int(float(note) / DACPEROCTAVE) > octave):
	    hints.append(i)
	    octave += 1
	i += 1

    # stringify

    table = ','.join(map(str, table)) 
    hints = ','.join(map(str, hints)) 

    outputhandle.write("// " + inputfile + "\n")
    outputhandle.write("// " + description + "\n")
    outputhandle.write("const float Quantizer::scale" + str(scalenum) + "[] = { " + table + " };" + "\n")
    outputhandle.write("const int Quantizer::hints" + str(scalenum) + "[] = { " + hints + " };" + "\n")

# MAIN

print "main"

argv = sys.argv[1:]

try:
    opts, args = getopt.getopt(argv,"i::",["input="])
except getopt.GetoptError:
    print "table_builder.py -i <inputfile>"
    sys.exit(2)

inputfile = "items.txt"

notecounter = []

for opt, arg in opts:
    if opt in ("-i", "--ifile"):
        inputfile = arg

print inputfile;

if inputfile == "":
    sys.exit(2)

i = 0

scales = []
hints = []

with open("scales.cpp", "w") as outputfile:
    with open(inputfile) as list:
	for item in list:
	    item = item.strip()
	    readFile(item, i, outputfile, notecounter)
	    scales.append('scale' + str(i))
	    hints.append('hints' + str(i))
	    i += 1

    notelist = ','.join(map(str, notecounter))
    scales = ','.join(map(str, scales))
    hints = ','.join(map(str, hints))

    outputfile.write("\n");
    outputfile.write("const int Quantizer::notecount[] = { " + notelist + " };" + "\n")
    outputfile.write("\n");
    
    outputfile.write("const float *Quantizer::scales[] = { " + scales + " };" + "\n")
    outputfile.write("const int *Quantizer::hints[] = { " + hints + " };" + "\n")
    
    outputfile.write("\n\n");
    outputfile.write("// for protected header\n");
    outputfile.write("const static int scaleCount = " + str(i) + ";\n");
    outputfile.write("static const int *hints[" + str(i) + "];\n");
    outputfile.write("static const float *scales[" + str(i) + "];\n");
    outputfile.write("static const int notecount[" + str(i) + "];\n");
    outputfile.write("\n");

    i = 0

    for notecount in notecounter:
	outputfile.write("static const float PROGMEM scale" + str(i) + "[" + str(notecount) + "];\n");
	outputfile.write("static const int PROGMEM hints" + str(i) + "[" + str(notecount) + "];\n");
	i += 1;


