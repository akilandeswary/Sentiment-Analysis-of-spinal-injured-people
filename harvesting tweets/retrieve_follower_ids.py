#Author: Akilandeswary Palaniappan
#Date  : 06/06/2015

#This program retrieves the follower ids of the spinal organisations
#and stores them in a file

import time
import tweepy
import couchdb
import json
import jsonpickle

#Authentication details of Twitter clients

#client 1
consumer_key1 = "L7T9BJkyDEFIQmv9Su3KQMSQs"
consumer_secret1 = "rm4fDrliQfLlPJrWGGdWmwW0TfqTw2HAMYfQdYtJ4nUBzoWFH8"
access_token1= "269568014-PNAbQy5wX8V1ieDXmiY4uwmr9ySnXjmp9PO4kD0t"
access_token_secret1 = "t26MtIY6hXue1Zect0mGgxbYCwscc1OC6ZnkWlzOmnEK3"

client1 = tweepy.OAuthHandler(consumer_key1, consumer_secret1)
client1.set_access_token(access_token1, access_token_secret1)

#client 2
consumer_key2 = "cfne9e8kuYdaSHFoWSxkSDXWt"
consumer_secret2 = "PkDn4Qg71iDuWBq0yq48PvJxA61z9Npq9avoGO9Tm9mz08qEtx"
access_token2= "3128899370-OX47fqscH6Ym7YYj8FJ6ANn7gHUF2GcWUtr2QRK"
access_token_secret2 = "7aqXIxexOzVD0sMrRoFxKXquOZ26X2U3e7mwO4zIBHqKK"

client2 = tweepy.OAuthHandler(consumer_key2, consumer_secret2)
client2.set_access_token(access_token2, access_token_secret2)

#client 3
consumer_key3 = "HnqNn34X2jW5F9d1bOULljYXm"
consumer_secret3 = "XGPT1so6xavZ9VZVEIbUGTDfyk9HfEMrJ56FhscYEj96xGVmUz"
access_token3= "3138438722-y5J74gtBPqcMwxtQ4WBASSsdJn3CRm8uXF5Fb0F"
access_token_secret3 = "UckRPyc06fOSOqS8HE8q3MY4Wk4N5xCTW1DcpsaI1TwOb"

client3 = tweepy.OAuthHandler(consumer_key3, consumer_secret3)
client3.set_access_token(access_token3, access_token_secret3)

#client 4
consumer_key4 = "vP86xZvOMEtcAlUcy6hYGx0Zp"
consumer_secret4 = "sMag2GsasoLW51ZjlzPPlSLfe6wOpTro7zokdyorkUFnYV1Whd"
access_token4= "3138450326-8jFkBdm61WwthnMwuOwnmcVAFmQ0mFcwumuX3uc"
access_token_secret4 = "HGpgN9v6vfyFtZIdCPMQAjsGIfhQzKWiRXEYYgtj0B0Qy"

client4 = tweepy.OAuthHandler(consumer_key4, consumer_secret4)
client4.set_access_token(access_token4, access_token_secret4)

client = []
client.append(client1)
client.append(client2)
client.append(client3)
client.append(client4)


auth = client[0]
api = tweepy.API(auth)
i=0

#Read spinal organisatins name from file to a list

orgList =[]
orgFile = open("spinal organisations.txt","r")
orgList= orgFile.read().split('\n')
orgFile.close()

idsList = []
ids_file = open("ids.txt", "a")

for name in orgList:
	try:
		print "retrieving follower ids of %s:"  % (name) 
		for page in tweepy.Cursor(api.followers_ids, screen_name=name).pages():
			idsList.extend(page)
	except:
		print "rate limit exceeded"
		if i==3:
			i=0
			print "waiting for 15 minutes"
			time.sleep(60*15)
		else:
			i=i+1
		print "changing account to client ",i
		auth = client[i]
		api= tweepy.API(auth)
			
#Write the follower ids to a file

for id in idsList:
	ids_file.writelines( "%s\n" % id)
	
print "total follwers id is:",len(idsList)
ids_file.close()







