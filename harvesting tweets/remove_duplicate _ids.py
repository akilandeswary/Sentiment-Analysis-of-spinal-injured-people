#Author: Akilandeswary Palaniappan
#Date  : 06/06/2015

#This program removes the duplicaes and returns unique ids

#Read follower ids from file to list

idsList=[]
idsFile = open("ids.txt","r")
idsList= idsFile.read().split('\n')
idsFile.close()

uniqueList =set(idsList)
print "number of unique ids",len(uniqueList)

uniqueIdsFile = open("unique_ids.txt", "a")

#Write uniwue ids to a file

for id in uniqueList:
	uniqueIdsFile.writelines( "%s\n" % id)
	
uniqueIdsFile.close()
