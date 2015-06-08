#Author: Akilandeswary Palaniappan
#Date  : 06/06/2015

#This program reads the coordinates of patient named 'Paul Mariager'
#and writes it into a file 

import json
import couchdb

couch = couchdb.Server()
db = couch['patients_with_polarity_db']

longArray=[]
latArray=[]

#retrive data from Pauls'scoordinates view

coordList = db.view('_design/test/_view/retrieve_Paul_coordinates',group=True)

for row in coordList:
	longitude= row.key[1][0]
	latitude = row.key[1][1]
	longArray.append(longitude)
	latArray.append(latitude)
	

#write data and cordinates to file

writeFile = open("Paul's coordinates.txt", "w")
for lon,lat in zip(longArray,latArray):
	writeFile.write(str(lat))
	writeFile.write(",")
	writeFile.write(str(lon))
	writeFile.write("\n")
writeFile.close()
