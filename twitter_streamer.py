import tweepy
import time
from twython import TwythonStreamer
from twython import Twython

MAXFILESIZE = 1024**3


consumer_key = 
consumer_secret =
access_token = 
access_token_secret = 

count = 0


api = None




   #Writes Tweet body to file until file size is reached.
def fileOut(data):

    f = open('UnicodeSample.txt' , 'a')

    f.write(str(data['text'].encode('utf-8')) + " | ")
    #print f.tell()
    if(f.tell() > MAXFILESIZE): #If greater than x file size quit
        f.close()
        print f.tell()
        quit()
    else:
        f.close()



   #Streamer from Twython
class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
           try:
               #print data['text'].encode('utf-8') #print to screen 
 
               fileOut(data)   #write to file
           except:
               pass
 
 
            #if ("qwer" in data['text'] and ('user' in data):
           # print data['user']['id']
           # print data['user']['screen_name'].encode('utf-8')
           # print data['user']['followers_count']
           # print data['lang']
            
            #for x in data:
              # if data[x] is not None:
               #   print "X IS: " + x + "  DATA IS: " +  str(data[x])


    def on_error(self, status_code, data):
        print "Stream Fail " + str(status_code)

        # Want to stop trying to get data because of the error?
        # Uncomment the next line!
        # self.disconnect()



stream = MyStreamer(consumer_key, consumer_secret,
                    access_token, access_token_secret)
#stream.statuses.filter(track='twitter')
#stream.statuses.filter(follow='some subscriber id goes here')
try:
    stream.statuses.sample()
except:
    pass




#-----------builds the followers string----------------
#auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
#auth.set_access_token(access_token, access_token_secret)

#api = tweepy.API(auth)

#g = open("idstring.txt" , 'r')
#mfollower = api.followers_ids("some subscriber name goes here")


#idString = g.read()

#idString = str(mfollower[0])

#for x in mfollower:
#    idString = idString + ',' + str(x) 

#g.write(idString)
#print idString


#stream.user()  #gets my account
#stream.statuses.filter()

#------------------------------------------------------











