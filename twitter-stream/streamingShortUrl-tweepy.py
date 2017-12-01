from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import datetime
import re
import sys

logFileData = datetime.datetime.now().strftime('%Y-%m-%d--%H-%M-%S')

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
        except KeyError:
            print("keyError")
        else:
            for url in re.findall(
                                      'https?://[\w:%#\$&\?\(\)~\.=\+\-]+/[\w/:%#\$&\?\(\)~\.=\+\-]+',
                                      tweet):
                print(url)
                #write log
                if len(sys.argv) >= 2:
                    f = open(sys.argv[1] + "-" + logFileData + ".txt", "a")
                    f.write(url + "\n")
        
        return True

    def on_error(self, status):
        print (status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=keywords, languages=["en"])
