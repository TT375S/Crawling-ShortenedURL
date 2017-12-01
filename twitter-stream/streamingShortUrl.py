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


while True:
    print("connecting...")
    auth = OAuth1(api_key, api_secret, access_token, access_secret)
    
    #r = requests.post(url, auth=auth, stream=True, data={"follow":"nasa9084","track":"emacs"})
    r = requests.post(url, auth=auth, stream=True, data={"track": keywords})


    for line in r.iter_lines():
        try:
            jsonData = json.loads(line.decode("utf-8"))
            print(jsonData["text"])
        except KeyError:
            print(traceback.format_exc())
            #KeyError occure if result is empty. So, wait to return results.
            time.sleep(10)
            continue
        except:
            print(traceback.format_exc())
            print("disconnect in 5 seconds")
            
            #may don't well work
            #disconnect
            #r = requests.post(url=url, auth=auth, stream=True, data={"track": keywords}, headers={'Connection':'close'})
            r = requests.post(url=url, data={"track": keywords}, headers={'Connection':'close'}) 
            time.sleep(10)
            #r = requests.post(url=url, data=body, headers={'Connection':'close'})
            #continue
            break
        else:
            #collect URL matched some patterns such as "http://aaa/aaaa" or "https://aaaaa/aa"
            for url in re.findall(
                    'https?://[\w:%#\$&\?\(\)~\.=\+\-]+/[\w/:%#\$&\?\(\)~\.=\+\-]+',
                    jsonData.get("text")):
                print(url)
                #write log
                if len(sys.argv) >= 2:
                    f = open(sys.argv[1] + "-" + logFileData + ".txt", "a")
                    f.write(url + "\n")
