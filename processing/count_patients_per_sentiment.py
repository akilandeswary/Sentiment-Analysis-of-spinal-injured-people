#Author: Akilandeswary Palaniappan
#Date  : 06/06/2015

#This program reads the patients file and 
#counts the number of patients per sentiment type 
#and calculates their percentage

from collections import Counter

with open("Patient_data_for_display_ver3.txt", "r") as readFile:
    lines = [tuple(line.split(',')) for line in readFile.readlines()]

countList=Counter(elem[4] for elem in lines)

#write counted values to the file 
#calculate percentage and write to file

countFile = open("count_sentiment_type.txt", "w")

for sentimentType,count in countList.iteritems():
    countFile.write( "{},{}\n".format(sentimentType,count))
for sentimentType,count in countList.iteritems():
	percent = (float(count)/70)*100
	countFile.write( "{},{}\n".format(sentimentType,percent))
 	
readFile.close()
countFile.close()
