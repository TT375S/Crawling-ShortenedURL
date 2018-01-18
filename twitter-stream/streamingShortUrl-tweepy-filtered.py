from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import datetime
import re
import sys
import http

logFileData = datetime.datetime.now().strftime('%Y-%m-%d--%H-%M-%S')

customTarget = ""
#correct only matched item
if len(sys.argv) >= 2:
    customTarget = sys.argv[1]
else:
    print("Filter keyword is empty. (argv[1])")

keywords = []
try:
    while (1):
        keywords.append(input())
except EOFError:
    pass


# consumer key, consumer secret, access token, access secret.
ckey  = ""
csecret = ""
atoken = ""
asecret = ""


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
    except KeyboardInterrupt:
        break
    except:
        continue
