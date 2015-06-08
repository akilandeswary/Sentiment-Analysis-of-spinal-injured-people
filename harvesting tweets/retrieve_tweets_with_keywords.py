#Author: Akilandeswary Palaniappan
#Date  : 06/06/2015

#This program retrieves tweets containing spinal injury related keywords

import json
import tweepy
import couchdb
import jsonpickle

class TweetStore(object):
	def __init__(self, dbname, url='http://127.0.0.1:5984/'):
		
		# Create a new database or open an existing one
		
		try:
		  self.server = couchdb.Server(url=url)
		  self.db = self.server.create(dbname)
		  
		except couchdb.http.PreconditionFailed:
		  self.db = self.server[dbname]
	  
	def save_tweet(self, tw):
		
		temp = jsonpickle.encode(tw)
		tempObj= json.loads(temp)
		tweet = tempObj['py/state']
		
		if 'id' in tweet and 'text' in tweet:
			
		#create a JSON document with only the tweet object
		
			doc={tweet['id']:tweet}
			docId,docRev = self.db.save(doc)
		else:
			print "Received a response that is not a tweet"
			print tweet
	  
storage = TweetStore('tweets_db')

#Authentication details of Twitter client

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

max_tweets =100

#Put search tags in a list

file1 = open('searchTags.txt', 'r')
tagsList= file1.read().split('\n')
file1.close()

#Open search loactions file

locFile = open('locations.txt', 'r')

client = []
client.append(client1)
client.append(client2)
client.append(client3)
client.append(client4)

auth = client[0]
api = tweepy.API(auth)
i=0

for name in locFile:
	for tags in tagsList:
		try:
			print "searching %s in %s:"  % (tags,name) 
			results= [status for status in tweepy.Cursor(api.search, q=tags,geocode = name).items(max_tweets)]
			for tweet in results:
				print tweet.text.encode("utf-8")
				storage.save_tweet(tweet)
		except:
			print "rate limit exceeded"
			if i==3:
				i=0
				#time.sleep(60*15)
			else:
				i=i+1
			print "changing account to client ",i
			auth = client[i]
			api= tweepy.API(auth)
			
locFile.close()

          





