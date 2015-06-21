# pip install Twython to get the twython module

import time
from twython import TwythonStreamer
from twython import Twython
import keys

MAXFILESIZE = 1024**3


consumer_key = keys.consumer_key
consumer_secret = keys.consumer_secret 
access_token = keys.access_token 
access_token_secret = keys.access_token_secret 

count = 0


api = None




   #Writes Tweet body to file until file size is reached.
def fileOut(data):

    f = open('ouput_twitter.json' , 'a')

    f.write(str(data))
    f.write(",\n")
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
        if True:
           try:
               #print data 
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
#stream.statuses.filter(follow='211972462')

print "Running"


with open('ouput_twitter.json' , 'a') as f:
    f.write('{\n\t"tweets": [\n')


try:
    stream.statuses.sample()
except(KeyboardInterrupt):
    with open('ouput_twitter.json' , 'a') as f:
        f.write("{}\n\t]\n}\n")




