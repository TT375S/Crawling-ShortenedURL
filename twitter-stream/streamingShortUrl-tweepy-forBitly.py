from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import datetime
import re
import sys
import http

logFileData = datetime.datetime.now().strftime('%Y-%m-%d--%H-%M-%S')

keywords = []
try:
    while (1):
        keywords.append(input())
except EOFError:
    pass


# consumer key, consumer secret, access token, access secret.
ckey  = "yjLJzAK41WfTd2uVT8BVvGzO2"
csecret = "M5Zq9pMDkOimNnRe64nwZn2N4o50QsEaqYBdo0M3GfWuOw5GDo"
atoken = "932179127355850753-DzumhDZea9KsnipPFJCgg1j225NJDCQ"
asecret = "algpNoTOJMwcT0Fbd3bUw5au3m5zdD968PITjgbBodtk5"


class listener(StreamListener):
    def on_data(self, data):
        all_data = json.loads(data)
        try:
            tweet = all_data["text"]
            #write URLs
            entities = all_data["entities"]
            urlDicts = entities["urls"]
            for urlDict in urlDicts:
                sURL = urlDict["url"] 
                dURL = urlDict["expanded_url"]
                print(sURL)
                print(dURL)
                
                #correct only matched item
                customTarget = "bit.ly"
                if not customTarget in dURL:
                    continue

                fs = open("sURL" + "-" + logFileData + ".txt", "a")
                fs.write(sURL + "\n")
                fd = open("dURL" + "-" + logFileData + ".txt", "a")
                fd.write(dURL + "\n")

        except KeyError:
            print("keyError")
        else:
            pass        
        return True

    def on_error(self, status):
        print (status)

def start_stream():
    while True:
        auth = OAuthHandler(ckey, csecret)
        auth.set_access_token(atoken, asecret)
        try:
            twitterStream = Stream(auth, listener())
            twitterStream.filter(track=keywords, languages=["en"])
        except http.client.IncompleteRead:
            print("IncompleteRead")
            continue

#In order to  catch ANY except by one try-catch...
while True:
    try:
        start_stream()
    except KeyInterrupt:
        break
    except:
        continue
