import json
with open('ouput_twitter.json' , 'r') as f:
    data = json.load(f)

print data

for tweet in data['tweets']:
    #check to see if 'text' key is in the tweet dict object
    #deleted tweets don't have a text key
    if  'text' in tweet:
        #to access the text value you index by the 'text' key. 
        #this is how you get to any of the data fields
        print tweet['text']

# a crapy way to see what keys are available for tweet dict objects
for tweet in data['tweets']:
    print tweet.keys()
