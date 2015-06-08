#Author: Akilandeswary Palaniappan
#Date  : 06/06/2015

#This program reads the patients file and 
#counts the number of patients per location

from collections import Counter

with open("Patient_data_for_display_ver4.txt", "r") as readFile:
    lines = [tuple(line.split(',')) for line in readFile.readlines()]

countList=Counter(elem[1] for elem in lines)

#write counted values to the file

countFile = open("patient_count_per_location.txt", "w")

for location,count in countList.iteritems():
    countFile.write( "{},{}\n".format(location,count) )
    	
readFile.close()
countFile.close()
