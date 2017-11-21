import requests
from requests_oauthlib import OAuth1
import json
import re
import sys
import datetime
import traceback
import urllib3
import http
import time 

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
    except:
        print(traceback.format_exc())
        time.sleep(5)
        continue
    else:
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

# except KeyError:
#     print("KeyError:  maybe connection broken")
#     time.sleep(20)
#     r = requests.post(url, auth=auth, stream=True, data={"track": keywords})
#     continue
# except http.client.IncompleteRead:
#     #except urllib3.exceptions.ProtocolError:
#     print("ProtocolError: maybe connection broken")
#     time.sleep(20)
#     r = requests.post(url, auth=auth, stream=True, data={"track": keywords})
#     continue

