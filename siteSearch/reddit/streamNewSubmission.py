import praw
import pprint
import re

keywords = []

try:
    while(1):
        keywords.append(input())
except EOFError:
    pass

reddit = praw.Reddit(client_id='oZAw',
                     client_secret='O8nj9yhq0',
                     user_agent='pytt3803',
                     username = 'kls',
                     password = 'q1'
                     )

print(reddit.read_only)

subreddit = reddit.subreddit('all')

for submission in subreddit.stream.submissions():
    submission.comments.replace_more(limit=0)
    all_comments = submission.comments.list()       # or the submission's URL if it's a self post

    #print(submission.selftext)

    #Search in submission body
    for keyword in keywords:
        foundUrls = re.findall('(?:https?:\/\/|)'+ keyword  +'\/[0-9a-zA-Z]+' , submission.selftext )
        for url in foundUrls:
            print(url)                 
    
    #Search in comments
    for comment in all_comments:
        for keyword in keywords:
            foundUrls = re.findall('(?:https?:\/\/|)'+ keyword  +'\/[0-9a-zA-Z]+' , comment.body )
            for url in foundUrls:
                print(url)                 
