#Author: Akilandeswary Palaniappan
#Date  : 06/06/2015

#This program reads the patients file,
#creates a summary of their attribtes,
#sort them based on location and sentiment type

import operator

#read patient file

with open("Patient_data_for_display_ver3.txt", "r") as readFile:
    lines = [tuple(line.split(',')) for line in readFile.readlines()]

#sort file according to location and sentiment 

sortedFile = open("patients_summary.txt", "w")
sortedMobilePatients = sorted(lines, key = operator.itemgetter(1,4))

#write sorted file 

sortedFile.write("Patient Name,Location,Follower Count, Friends Count,Tweet Count, Retweet Count, Mobility, Sentiment")
sortedFile.write("\n")
for tuple in sortedMobilePatients:
    sortedFile.write ("\"%s\",\"%s\",%s,%s,%s,%s,\"%s\",\"%s\"" % (tuple[0],tuple[1],tuple[6],tuple[8],tuple[2],tuple[7],tuple[5],tuple[4]))
    sortedFile.write("\n")
    
#close files

readFile.close()
sortedFile.close()
