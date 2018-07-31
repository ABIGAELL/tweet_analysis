
import json
from textblob import TextBlob
import matplotlib.pyplot as plt

#Get the JSON data
tweetFile = open("tweets.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

polarityList=[]
subjectivityList=[]

# Continue your program below!
for tweet in tweetData:
	print(tweet)
    break
