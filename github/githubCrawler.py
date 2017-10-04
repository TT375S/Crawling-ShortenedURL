# -*- coding: utf-8 -*-

#なんか検索画面に表示されるコードの取得が上手くいかない(JSかなんかで後からレンダリングされてるかShadow DOMとやらなのかよくわからんけど)のでやっぱりヘッドレスブラウザを使うことにしてコレは無かったことにします

import urllib.parse
import urllib.request
import re
import sys
import time

searchType = ["Code", "Commits", "Issues", "Wikis", "Users"]

try:
    while(1):
        targetShortURLDomain = input()
        
        #Github can search Code, Commits, Issues, etc...
        for stype in searchType:
            #Page number of search screen.
            for pageNum in range(1, 10):
                #IMPORTANT: urllib.request encodes the target URL with ASCII. 
                # If the URL contains non-ascii character, it should be encoded with UTF-8 by using urllib.parse.
                url = "http://github.com/search?p="+str(pageNum)+"&utf8=✓&q="+targetShortURLDomain+"&type=" + stype
                print(url, file=sys.stderr)
                
                with urllib.request.urlopen(urllib.parse.quote_plus(url, "/:?=&")) as response:
                    html = response.read().decode('utf-8')
                    print(html)
                    shortURLs = re.findall(targetShortURLDomain + '/[0-9a-zA-Z]+', html)
                    undup = set(shortURLs)
                    for shortURL in undup:
                        print(shortURL)
                #Avoid "Too many request" error.
                time.sleep(2)
except EOFError:
    pass

