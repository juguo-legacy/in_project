#!/usr/bin/env python3
import sys
import os
import os.path

curdirectory = "./"

try:
    with open("data/"+sys.argv[1]+".in", "r") as fin:
        lines = fin.readlines()
except:
    raise ValueError("No Input or Invalid Input Given.  Run the file with ./replaceinput.py [number]")

files_in_directory = os.listdir(curdirectory)
for i in files_in_directory:
    if i.endswith(".in"):
        with open(i, "w") as fout:
            for j in range(len(lines)):
                fout.write(lines[j])
        print("Successfully copied to "+str(i)+"!")
        break