#!/usr/bin/python

# Quantizer
# Rich Holmes
# 
# Based on:
# table_builder.py from https://github.com/bpcmusic/telex_scales
#
# Removed frequency table, added PROGMEM to declarations.
#
#
# Added organization of scales into banks.
#
# In the absences of commands to the contrary each scale is assigned
# to be the next scale in the same bank as the previous; first scale is
# bank 1 (index 0), scale 1 (index 0)
#
# Use commands to change:
#
# +b <bank> [#description]
# Append next scale to bank #<bank> (index <bank>-1) with given description
# Description overwrites previous description if given
#
# +s <scale> 
#
# Assign next scale to scale number <scale> (index <scale>-1)
#
# +d <bank1> <scale1> <bank2> <scale2>
#
# Duplicate scale at bank <bank1>, scale <scale1> to bank <bank2>, scale <scale2>
# (Dupicate entries made in bank/scale table, the scale data itself is not
# duplicated.)
#
#
# Added capability to generate scales as well as reading them
# Input file lines can be:
# <path to scl file> [#description]
# or
# +g <n> <generator> [<period>] [#description]
# or
# +e <n> [list of numbers] [#description]
# or
# +q <n> <period> [list of numbers] [#description]
#
# Description if present in the first of these overrides the description in the file.
#
# Second of these means to generate a scale with n notes using
# generator and period. E.g.:
#
# +g 12 3/2 2/1
#
# for a 12-tone Pythagorean scale. If the period is omitted, 2/1 is the default.
#
# Third means to generate a scale using the listed entries (indexed from 0) from
# an n-equal division of the octave. 0 is always assumed. E.g.:
#
# +e 12 2 4 5 7 9 11
#
# for a 12-equal major scale. If the list is omitted, the scale contains all
# n notes.
#
# +q is the same as +e except a period to be equally divided is given. E.g.,
# +q 13 3/1 for Bohlen-Pierce equal temperament.
#
# Script has minimal error checking so far!!

import sys, getopt, math

DACTOP = 4095   # limit of DAC (2**12-1)
DAC1   = 4095   # DAC counts corresponding to defined voltage
V1     = 5.0    # voltage corresponding to DAC1
DACPEROCTAVE  = (DAC1/V1)  # DAC counts per octave

import sys, getopt, math

def realOrRat (item):
    if "/" in item:
        ratio = item.split("/")
	value = float(ratio[0]) / float(ratio[1])
	value = math.log(value) * 1200 / math.log(2)
    else:
        value = float(item)
    return value

def onescale(item, scalenum, outputhandle, notecounter):
    print item
    description = ""
    values = 0
    scale = []
    generator = 0.0
    period = 1200.0

    if "#" in item:
        items = item.split ("#")
        description = items[1]
        item = items[0]
    
    if item.startswith ("+g"):
        items = item.split ()
        n = int(items[1])
        generator = realOrRat(items[2])
        if len(items) > 3:
            period = realOrRat(items[3])
        else:
            period = 1200.0
        value = generator
        scale = [1200.0]
        while len(scale) < n:
            while value > period:
                value -= period
            scale.append (value)
            value += generator
        scale.sort()
    elif item.startswith ("+e") or item.startswith ("+q"):
        items = item.split ()
        n = int(items[1])
        if items[0].startswith ("+e"):
            period = 1200.0
            if len(items) > 2:
                elist = [int(i) for i in items[2:]]
            else:
                elist = range(0,n)
        else:
            period = realOrRat(items[2])
            if len(items) > 3:
                elist = [int(i) for i in items[3:]]
            else:
                elist = range(0,n)

        
        cscale = [period/n*i for i in range (0, n)]

        scale = []
        for e in elist:
            if not (cscale[e] == 0):
                scale.append (cscale[e])
        scale.append (period) 
    else:
        with open(item) as f:
            for line in f:
                line = line.strip()

                # if it is a comment - skip it
                if line.startswith("!"):
                    continue

                if description == "":
                    description = line
                elif values == 0:
                    values = int(line)
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

    outputhandle.write("// " + str(scalenum) + " | " + item + " | " + description + "\n")
    outputhandle.write("const float Quantizer::scale" + str(scalenum) + "[] = { " + table + " };" + "\n")
    outputhandle.write("const int Quantizer::hints" + str(scalenum) + "[] = { " + hints + " };" + "\n")

# MAIN

argv = sys.argv[1:]

try:
    opts, args = getopt.getopt(argv,"i::",["input="])
except getopt.GetoptError:
    print "table_builder.py -i <inputfile>"
    sys.exit(2)

inputfile = "items.txt"

notecounter = []
scales = []
hints = []
nbank = 6  # number of banks
nscale = 12  # number of scales per bank
bankandscale = [[-1 for i in range(nscale)] for j in range(nbank)]
lastscalesofar = [-1 for i in range(nbank)] # last scale index used so far in each bank
bankdesc = ["" for i in range(nbank)]

for opt, arg in opts:
    if opt in ("-i", "--ifile"):
        inputfile = arg

if inputfile == "":
    sys.exit(2)

i = 0
curbank = 0  # index
curscale = 0  # index

with open("scales.cpp", "w") as outputfile:
    with open(inputfile) as list:
	for item in list:
	    item = item.strip()
            # Check if it's a command rather than a scale definition
            if item.startswith ("+b") or item.startswith ("+s") or item.startswith ("+d"):
                print item
                description = ""
                if "#" in item:
                    items = item.split ("#")
                    description = items[1]
                    item = items[0]
                items = item.split ()
                if items[0] == "+b":
                    # Change bank assignment for next scale
                    curbank = int(items[1]) - 1
                    if not (description == ""):
                        bankdesc[curbank] = description
                    curscale = lastscalesofar[curbank] + 1
                if items[0] == "+s":
                    # Change scale assignment for next scale
                    curscale = int(items[1]) - 1
                if items[0] == "+d":
                    # Duplicate a bank assignment
                    obank = int(items[1])-1
                    oscale = int(items[2])-1
                    dbank = int(items[3])-1
                    dscale = int(items[4])-1
                    bankandscale[dbank][dscale] = bankandscale[obank][oscale]
                    if dscale > lastscalesofar[dbank]:
                        lastscalesofar[dbank] = dscale
            else:
	        onescale(item, i, outputfile, notecounter)
	        scales.append('scale' + str(i))
	        hints.append('hints' + str(i))
                bankandscale[curbank][curscale] = i
                curscale += 1
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
    outputfile.write("const int Quantizer::bankandscale[" + str(nbank) + "][" + str(nscale) + "] = {\n")
    for b in range (nbank):
        outputfile.write ("  {")
        for s in range (nscale-1):
            outputfile.write (" {:3d},".format(bankandscale[b][s]))
        outputfile.write (" {:3d}".format(bankandscale[b][nscale-1]))
        outputfile.write (" }" + ("," if b < nbank-1 else " "))
        outputfile.write (" // {:2d}".format(b+1))
        if not bankdesc[b] == "":
            outputfile.write (" " + bankdesc[b])
        outputfile.write ("\n")

    outputfile.write("};\n\n");
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


