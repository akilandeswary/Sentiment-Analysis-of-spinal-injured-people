#Author: Akilandeswary Palaniappan
#Date  : 06/06/2015

#This program reads the patients file and 
#sorts it based on the mobile type and sentiment type

import operator

#read patients file
with open("Patient_data_for_display_ver3.txt", "r") as readFile:
    lines = [tuple(line.split(',')) for line in readFile.readlines()]

#sort file
sortedFile = open("mobile_patients_list.txt", "w")
sortedMobilePatients = sorted(lines, key = operator.itemgetter(4, 5))

#write sorted patients file 
for tuple in sortedMobilePatients:
    sortedFile.write ("%s,%s,%s,%s,%s,%s" % tuple)

#close files
readFile.close()
sortedFile.close()
