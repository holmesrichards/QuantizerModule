#!/usr/bin/python

import os, sys

path = "./scl/"
dirs = os.listdir( path )

index = []

n = 7

for file in dirs:
   with open(path+file) as f: 
       desc = ""
       n = 0
       first_n = ""
       i = 0
       for line in f: 
           if line[0] == "!":
               continue
           elif desc == "":
               desc = line
           elif n == 0:
               n = int(line)
           else:
               first_n += " " + line.rstrip()
               i = i + 1
               if i >= n:
                   index.append ("{:5d}\t{:s}".format (n, first_n + " " + file))
                   break

for i in sorted(index):
    print i
    
