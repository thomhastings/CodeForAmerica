#!/usr/bin/env python
import datetime

# Declare variable
categories = []

# Parse input file
inputfile = open("Violations-2012.csv", "r")
inputfile.readline() # get buffer past headings
line = inputfile.readline()
while line:
    values = line.split(",")
    if values[2] not in categories:
        categories.append(values[2])
        categories.append([datetime.datetime.strptime(values[3].split(" ")[0], "%Y-%m-%d")])
    else:
        categories[categories.index(values[2])+1].append(datetime.datetime.strptime(values[3].split(" ")[0], "%Y-%m-%d"))
    line = inputfile.readline()

# Print output
for item in categories:
    if isinstance(item, str):
        print "\nCategory:\t" + item
    else:
        print "Occurences:\t" + str(len(item))
        print "First:\t" + str(min(item))
        print "Last:\t" + str(max(item))
