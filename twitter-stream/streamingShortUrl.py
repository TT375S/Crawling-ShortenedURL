import requests
from requests_oauthlib import OAuth1
import json
import re
import sys
import datetime
import traceback

logFileData = datetime.datetime.now().strftime('%Y-%m-%d--%H-%M-%S')

keywords = []
try:
    while (1):
        keywords.append(input())
except EOFError:
    pass

#COMPLETE BELOW 4 PARAM
api_key = ""
api_secret = ""
access_token = ""
access_secret = ""

url = "https://stream.twitter.com/1.1/statuses/filter.json"

auth = OAuth1(api_key, api_secret, access_token, access_secret)

#r = requests.post(url, auth=auth, stream=True, data={"follow":"nasa9084","track":"emacs"})
r = requests.post(url, auth=auth, stream=True, data={"track": keywords})


for line in r.iter_lines():
    try:
        jsonData = json.loads(line.decode())
        print(jsonData["text"])

        #collect URL matched some patterns such as "http://aaa/aaaa" or "https://aaaaa/aa"
        for url in re.findall(
                'https?://[\w:%#\$&\?\(\)~\.=\+\-]+/[\w/:%#\$&\?\(\)~\.=\+\-]+',
                jsonData["text"]):
            print(url)
            #write log
            if len(sys.argv) >= 2:
                f = open(sys.argv[1] + "-" + logFileData + ".txt", "a")
                f.write(url + "\n")
                f.close()

    except:
        print(traceback.format_exc())



