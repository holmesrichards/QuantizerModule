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
# +g <n> <generator> [<period>] [<firstnote>] [#description]
# or
# +e <n> [list of numbers] [#description]
# or
# +q <n> <period> [list of numbers] [#description]
#
# Description if present in the first of these overrides the description in the file.
#
# Second of these means to generate a scale with n notes using
# generator and period starting from given firstnote . E.g.:
#
# +g 12 3/2 2/1 500
#
# for a 12-tone Pythagorean scale. Parameters can be ratios or cents.
# If the period is omitted, 2/1 is the default.
# If firstnote is omitted, 0 is the default.
#
# Third means to generate a scale using the listed entries (indexed from 0) from
# an n-equal division of the octave. 0 is NOT assumed. E.g.:
#
# +e 12 0 2 4 5 7 9 11
#
# for a 12-equal major scale. If the list is omitted, the scale contains all
# n notes.
#
# +q is the same as +e except a period to be equally divided is given. E.g.,
# +q 13 3/1 for Bohlen-Pierce equal temperament.
#
# Script has minimal error checking so far!!

import sys, getopt, math, re

DACTOP = 2047   # limit of DAC (2**11-1, we only cover 0 to 5 volts)
DAC1   = 4095   # DAC counts corresponding to defined voltage
V1     = 10.0    # voltage corresponding to DAC1
DACPEROCTAVE  = (DAC1/V1)  # DAC counts per octave

NBANK = 6  # number of banks
NSCALE = 12  # number of scales per bank

import sys, getopt, math

def checkBS (b, s, item):
    if b < 0 or b >= NBANK:
        print "!!!!! For '"+item+"' bank", b+1, "out of range"
        exit()
    if s < 0 or s >= NSCALE:
        print "!!!!! For '"+item+"' scale", s+1, "out of range"
        exit()
    return True

def realOrRat (item):
    # Return float(item) unless we think it's a representation of a rational,
    # else compute the value of the rational, convert to cents, and
    # return that
    if "/" in item:
        ratio = item.split("/")
	value = float(ratio[0]) / float(ratio[1])
	value = math.log(value) * 1200 / math.log(2)
    else:
        value = float(item)
    return value

def onescale(item, scalenum, outputhandle, notecounter):
    # Generate one scale
    print item
    description = ""
    values = 0
    scale = [] # this will become a sorted list of all notes in one period
    generator = 0.0
    period = 1200.0

    if "#" in item:
        items = item.split ("#", 1)
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
        if len(items) > 4:
            firstnote = realOrRat(items[4])
        else:
            firstnote = 0.0
        value = firstnote
        scale = []
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
            scale.append (cscale[e])
        scale.sort()
    else:
        # Read Scala scale which always ends with period
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
        period = scale[-1]
        scale = [0] + scale[0:-1]
        
    table = []

    print "period", period, "scale", scale
    
    # Make table of scale notes by looping over the scale in both directions
    # with given period until we go below 0 and above DACTOP
    centstodac = DACPEROCTAVE / 1200.
    dacs = 0.

    note = len(scale)-1
    octave = -period
    while True:
	dacs = (scale[note] + octave) * centstodac
	table.append(dacs)
        if dacs <= 0:
            break
	note -= 1
	if note < 0:
	    octave -= period
	    note = len(scale)-1

    note = 0
    octave = 0
    while True:
	dacs = (scale[note] + octave) * centstodac
	table.append(dacs)
        if dacs >= DACTOP:
            break;
	note += 1
	if note >= len(scale):
	    octave += period
	    note = 0

    while len(table) > 1 and table[1] <= 0:
        table = table[1:]
    while len(table) > 1 and table[len(table)-2] >= DACTOP:
        table = table[:-2]
        
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
    print "table_builder.py -i <inputfilepath>"
    sys.exit(2)

inputfilepath = "items.txt"

notecounter = []
scales = []
hints = []
bankandscale = [[-1 for i in range(NSCALE)] for j in range(NBANK)]
lastscalesofar = [-1 for i in range(NBANK)] # last scale index used so far in each bank
bankdesc = ["" for i in range(NBANK)]

for opt, arg in opts:
    if opt in ("-i", "--ifile"):
        inputfilepath = arg

if inputfilepath == "":
    sys.exit(2)

outputfilepath = re.sub("\..*", "", inputfilepath);
outputfilepath += ".cpp"

i = 0
curbank = 0  # index
curscale = 0  # index

with open(outputfilepath, "w") as outputfile:
    with open(inputfilepath) as inputfile:
	for item in inputfile:
            if item.startswith ("#"):
                continue
	    item = item.strip()
            # Check if it's a command rather than a scale definition
            if item.startswith ("+b") or item.startswith ("+s") or item.startswith ("+d"):
                print item
                description = ""
                if "#" in item:
                    items = item.split ("#", 1)
                    description = items[1]
                    item = items[0]
                items = item.split ()
                if items[0] == "+b":
                    # Change bank assignment for next scale
                    curbank = int(items[1]) - 1
                    if checkBS (curbank, 0, item):
                        if not (description == ""):
                            bankdesc[curbank] = description
                        curscale = lastscalesofar[curbank] + 1
                if items[0] == "+s":
                    # Change scale assignment for next scale
                    if checkBS (0, curscale, item):
                        curscale = int(items[1]) - 1
                if items[0] == "+d":
                    # Duplicate a bank assignment
                    obank = int(items[1])-1
                    oscale = int(items[2])-1
                    dbank = int(items[3])-1
                    dscale = int(items[4])-1
                    if checkBS (obank, oscale, item) and checkBS (dbank, dscale, item):
                        bankandscale[dbank][dscale] = bankandscale[obank][oscale]
                        if dscale > lastscalesofar[dbank]:
                            lastscalesofar[dbank] = dscale
            else:
	        onescale(item, i, outputfile, notecounter)
	        scales.append('scale' + str(i))
	        hints.append('hints' + str(i))
                if checkBS (curbank, curscale, item):
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
    outputfile.write("const int Quantizer::bankandscale[" + str(NBANK) + "][" + str(NSCALE) + "] = {\n")
    for b in range (NBANK):
        outputfile.write ("  {")
        for s in range (NSCALE-1):
            outputfile.write (" {:3d},".format(bankandscale[b][s]))
        outputfile.write (" {:3d}".format(bankandscale[b][NSCALE-1]))
        outputfile.write (" }" + ("," if b < NBANK-1 else " "))
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


