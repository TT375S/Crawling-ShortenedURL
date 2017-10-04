# -*- coding: utf-8 -*-

import urllib.parse
import urllib.request
import urllib.error
import re
import sys
import time
import itertools
import string

import urllib.parse
import urllib.request

#Listed 0-9 a-z A-Z
challengeChar = []
for i in range(0,10):
    challengeChar.append(str(i))
for i in string.ascii_lowercase[:26]:
    challengeChar.append(i)
for i in string.ascii_uppercase[:26]:
    challengeChar.append(i)

#Google shortener API key
print("Input Google shortener API key", sys.stderr)
APIKey = input()


for length in range(3, 10):
    #repeated permutation of [0-9a-zA-Z].
    challengeTexts = list(itertools.product(challengeChar, repeat=length) )

    #print(challengeTexts)
    for challengeText in challengeTexts:
        #Free API key is restricted req rate, 1 request/sec.
        time.sleep(1)
        
        url = "https://www.googleapis.com/urlshortener/v1/url?shortUrl=http://goo.gl/"+"".join(challengeText) +"&projection=FULL&key=" + APIKey
        print(url, file=sys.stderr)
        try:
            with urllib.request.urlopen(urllib.parse.quote_plus(url, "/:?=&")) as response:
                res = response.read().decode('utf-8')
                print(res)
            
            if "error" in res:
                pass
            else:
                print("".join(challengeText))
                print("HIT", sys.stderr)
        except urllib.error.HTTPError:
            print("404", sys.stderr) 
                
