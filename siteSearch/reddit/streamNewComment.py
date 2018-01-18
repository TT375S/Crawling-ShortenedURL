import praw
import pprint
import calendar
import re
keywords = []

try:
    while(1):
        keywords.append(input())
except EOFError:
    pass

reddit = praw.Reddit(client_id='oZAw',
                     client_secret='9yhq0',
                     user_agent='03',
                     username = '',
                     password = '1'
                     )

print(reddit.read_only)

subreddit = reddit.subreddit('all')

for comment in subreddit.stream.comments():

    print(comment.body)

    for keyword in keywords:
        foundUrls = re.findall('(?:https?:\/\/|)'+ keyword  +'\/[0-9a-zA-Z]+' , comment.body )
        for url in foundUrls:
            print(url)                 
