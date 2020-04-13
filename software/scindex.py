#!/usr/bin/python

import os, sys

# Open a file
path = "./scl/"
dirs = os.listdir( path )

index = []

# This would print all the files and directories
for file in dirs:
   with open(path+file) as f: 
       desc = ""
       n = 0
       first5 = ""
       i = 0
       for line in f: 
           if line[0] == "!":
               continue
           elif desc == "":
               desc = line
           elif n == 0:
               n = int(line)
           else:
               first5 += " " + line.rstrip()
               i = i + 1
               if i >= 5:
                   index.append ("{:5d}\t{:s}".format (n, first5 + " " + file))
                   break

for i in sorted(index):
    print i
    
