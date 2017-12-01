from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json


# consumer key, consumer secret, access token, access secret.
ckey  = ""
csecret = ""
atoken = ""
asecret = ""


class listener(StreamListener):
    def on_data(self, data):
        all_data = json.loads(data)
        tweet = all_data["text"]
        out = open('verizon_twitter_data.txt', 'a+')
        tweet=tweet.encode('utf-8')
        out.write(str(tweet)+"\n")

        print (tweet)

        out.close()
        return True

    def on_error(self, status):
        print (status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=['verizon', 'vzw','verizzon',    'vrizon','verizonfois',
                        'verzon','verizun','vrzon','veerizon','verrizon', 'veriizon'], languages=["en"])
