#Author: Akilandeswary Palaniappan
#Date  : 06/06/2015

#This program reads the patients file and 
#counts the occurence of each type of mobilty type

from collections import Counter

with open("Patient_data_for_display_ver3.txt", "r") as readFile:
    lines = [tuple(line.split(',')) for line in readFile.readlines()]

countList=Counter(elem[5] for elem in lines)

#write counted values to the file

countFile = open("count_mobility_type.txt", "w")

for mobilityType,count in countList.iteritems():
    countFile.write( "{},{}\n".format(mobilityType,count))

readFile.close()
countFile.close()
