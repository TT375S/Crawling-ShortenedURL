import datetime
def writeLineOpenAndClose(fileName, mode, content):
    f = open(fileName, mode)
    f.write(content+"\n")
    f.close()

logFileData = datetime.datetime.now().strftime('%Y-%m-%d--%H-%M-%S')

#most of this script came from https://www.karambelkar.info/2015/01/how-to-use-twitters-search-rest-api-most-effectively./
import tweepy
from tweepy import OAuthHandler

# Replace the API_KEY and API_SECRET with your application's key and secret.
ckey  = ""
csecret = ""
atoken = ""
asecret = ""


auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
# OAuth
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

if (not api):
    print ("Can't Authenticate")
    sys.exit(-1)

import sys
import jsonpickle
import os

searchQuery = 'http'  # this is what we're searching for
maxTweets = 10000000  # Some arbitrary large number
tweetsPerQry = 100    # this is the max the API permits
fName = "tweets"+logFileData+".txt"  # We'll store the tweets in a text file.


# If results from a specific ID onwards are reqd, set since_id to that ID.
# else default to no lower limit, go as far back as API allows
sinceId = None

# If results only below a specific ID are, set max_id to that ID.
# else default to no upper limit, start from the most recent tweet matching the search query.
max_id = -1

tweetCount = 0
print("Downloading max {0} tweets".format(maxTweets))
with open(fName, 'w') as f:
    while tweetCount < maxTweets:
        try:
            if (max_id <= 0):
                if (not sinceId):
                    new_tweets = api.search(q=searchQuery, count=tweetsPerQry)
                else:
                    new_tweets = api.search(q=searchQuery, count=tweetsPerQry,
                                            since_id=sinceId)
            else:
                if (not sinceId):
                    new_tweets = api.search(q=searchQuery, count=tweetsPerQry,
                                            max_id=str(max_id - 1))
                else:
                    new_tweets = api.search(q=searchQuery, count=tweetsPerQry,
                                            max_id=str(max_id - 1),
                                            since_id=sinceId)
            if not new_tweets:
                print("No more tweets found")
                break
            #process tweets
            for tweet in new_tweets:
                #print(tweet.user.name)
                #print(tweet.user.screen_name)
                #print(tweet.text)
                #print(tweet.created_at+ datetime.timedelta(hours=9))
                urlDict = tweet.entities["urls"]
                for urlEntry in urlDict:
                    sURL = urlEntry["url"]
                    dURL = urlEntry["expanded_url"]
                    print(sURL)
                    print(dURL)
                    writeLineOpenAndClose("sURL-"+logFileData+".txt", "a", sURL)
                    writeLineOpenAndClose("dURL-"+logFileData+".txt", "a", dURL)
                f.write(jsonpickle.encode(tweet._json, unpicklable=False) +
                        '\n')
            tweetCount += len(new_tweets)
            print("Downloaded {0} tweets".format(tweetCount))
            max_id = new_tweets[-1].id
        except tweepy.TweepError as e:
            # Just exit if any error
            print("some error : " + str(e))
            break

print ("Downloaded {0} tweets, Saved to {1}".format(tweetCount, fName))

