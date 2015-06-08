#Author: Akilandeswary Palaniappan
#Date  : 06/06/2015

#This program harvests the tweets from Twitter using user name.
#It also calculates the sentiment polarity for each tweet,
#adds it with the tweet object and stores it in CouchDB

import json
import time
import tweepy
import tweepy
import couchdb
import simplejson
import jsonpickle
from textblob import TextBlob

class TweetStore(object):
	def __init__(self, dbname, url='http://127.0.0.1:5984/'):
		
		#Create a new database or open an existing one
		try:
		  self.server = couchdb.Server(url=url)
		  self.db = self.server.create(dbname)
		except couchdb.http.PreconditionFailed:
		  self.db = self.server[dbname]
	  
	def save_tweet_and_sentiment(self, twitterObj):
		
		#Find polarity of tweet text
		tempTweet= TextBlob(twitterObj.text)
		polarity = tempTweet.sentiment.polarity
		
		#Create sentiment polarity object
		pol = {}
		pol['tweet_sentiment'] = polarity
		polObj = json.dumps(pol)
		polObj = json.loads(polObj)
		
		#Create tweet Object
		tweetString = jsonpickle.encode(tweet)
		jsonString = json.loads(tweetString)
		tweetText = jsonString['py/state']['_json']
		jsonObj= json.dumps(tweetText)
		jsonObj2 = json.loads(jsonObj)
		
		#Merge both objects	
		finalObj = dict(jsonObj2.items()+ polObj.items())
		
		#Store merged object in CouchDB
		self.db.save(finalObj)
		
#Create database handler	  
storage = TweetStore('patients_with_polarity_db')	

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

#Read names of spinal Injured people from file into a list

file1 = open('spinalInjuredPeople.txt', 'r')
nameList= file1.read().split('\n')
file1.close()

client = []
client.append(client1)
client.append(client2)
client.append(client3)
client.append(client4)

auth = client[0]
api = tweepy.API(auth)
i=0

#Harvesting and storing tweets
for name in nameList:
	print "retrieving  tweets of %s:"  % (name)

	#Initialize a list to hold all the tweepy Tweets
	alltweets = []	
	
	try:
	
		#Make initial request for most recent tweets (200 is the maximum allowed count)
		newTweets = api.user_timeline(screen_name = name,count=200)
		
		for tweet in newTweets:
			storage.save_tweet_and_sentiment(tweet)
									
		#save most recent tweets
		alltweets.extend(newTweets)
		
		#save the id of the oldest tweet less one
		oldest = alltweets[-1].id - 1
		
		#keep grabbing tweets until there are no tweets left to grab
		while len(newTweets) > 0:
			print "getting tweets before %s" % (oldest)
			
			#all subsequent requests use the max_id param to prevent duplicates
			newTweets = api.user_timeline(screen_name = name,count=200,max_id=oldest)
		
			for tweet in newTweets:
				storage.save_tweet_and_sentiment(tweet)
							
			#save most recent tweets
			alltweets.extend(newTweets)
			
			#update the id of the oldest tweet less one
			oldest = alltweets[-1].id - 1
			
			print "...%s tweets downloaded so far" % (len(alltweets))
					
	except:
		
		print "rate limit exceeded"
		if i==3:
			print "waiting for 15 min"
			i=0
			time.sleep(60*15)
		else:
			i=i+1
		print "changing account to client ",i
		auth = client[i]
		api= tweepy.API(auth)
	

