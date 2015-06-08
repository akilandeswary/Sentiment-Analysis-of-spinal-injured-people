#Author: Akilandeswary Palaniappan
#Date  : 06/06/2015

#This program creates a patient file by reading the CouchDB views
#calculates sentiment polarity ratio and
#assigns the respective sentiment type to each patient 

import json
import couchdb
import operator
from operator import itemgetter

#create CouchDB handler

couch = couchdb.Server()
db = couch['patients_with_polarity_db']
print db.name

countArray=[]
namesArray=[]
polArray =[]
ratioArray=[]
sentimentTypeArray=[]
tweetCountArray=[]
lines=()

#retrive tweet count as a float value from view into an countArray

countList = db.view('_design/test/_view/display_tweet_count',group=True)

for row in countList:
	countArray.append(float(row.value))
	temp= row.key.encode("utf-8")
	namesArray.append(temp)

#retrieve polarity from view into polArray

polList = db.view('_design/test/_view/display_polarity',group=True)
for row in polList:
	polArray.append(float(row.value))
	
#retrieve tweet count as an integer into tweetCountArray

tweetCountList = db.view('_design/test/_view/display_tweet_count',group=True)
for row in tweetCountList:
	tweetCountArray.append(int(row.value))

#calculate sentiment polarity ratio and output into ratioArray

for (p,c) in zip(polArray, countArray):
	r=p/c
	ratioArray.append(r)
	
	if r>0:
		if r>=0.25:
			sentimentTypeArray.append('Most Positive')
		else:
			sentimentTypeArray.append('Positive')
	else:
		if r<0:
			if r<=-0.25:
				sentimentTypeArray.append('Most Negative')
			else:
				sentimentTypeArray.append('Negative')
		else:
			sentimentTypeArray.append('Neutral')
	
			
		
#write patient details into file

writeFile = open("patient_data_for_display.txt", "w")
for (s,r,c,n) in zip(sentimentTypeArray,ratioArray,tweetCountArray,namesArray):
	writeFile.write(n)
	writeFile.write(",")
	writeFile.write(str(c))
	writeFile.write(",")
	writeFile.write(str(r))
	writeFile.write(",")
	writeFile.write(s)
	writeFile.write("\n")
writeFile.close()


