import praw
import pprint
import calendar
import datetime
import re

# UTC の naive オブジェクト
now = datetime.datetime.utcnow()
print(now)
# UTC の naive オブジェクト -> Unix time
unix = calendar.timegm(now.utctimetuple())
print(unix)


keywords = ["biy.ly," "goo.gl", "tinyurl.com"]

reddit = praw.Reddit(client_id='oZAw',
                     client_secret='hq0',
                     user_agent='3',
                     username = '3',
                     password = ''
                     )

print(reddit.read_only)

# assume you have a Reddit instance bound to variable `reddit`
subreddit = reddit.subreddit('all')

#print(subreddit.display_name)  # Output: redditdev
#print(subreddit.title)         # Output: reddit Development
#print(subreddit.description)   # Output: A subreddit for discussion of ...


#pprint.pprint(vars(subreddit))

# assume you have a Subreddit instance bound to variable `subreddit`
for submission in subreddit.new(limit=100):
    #print(submission.title)  # Output: the submission's title
    #print(submission.score)  # Output: the submission's score
    #print(submission.id)     # Output: the submission's ID
    #print(submission.url)    # Output: the URL the submission points to
    submission.comments.replace_more(limit=0)
    all_comments = submission.comments.list()       # or the submission's URL if it's a self post
    #pprint.pprint(dir(all_comments))a

    for keyword in keywords:
        foundUrls = re.findall('(?:https?:\/\/|)'+ keyword  +'\/[0-9a-zA-Z]+' , submission.selftext )
        for url in foundUrls:
            print(url)                 
    
    for comment in all_comments:
        #print(comment.body)
        for keyword in keywords:
            foundUrls = re.findall('(?:https?:\/\/|)'+ keyword  +'\/[0-9a-zA-Z]+' , comment.body )
            for url in foundUrls:
                print(url)                 
    #pprint.pprint(vars(submission))
    #print(submission.selftext)
