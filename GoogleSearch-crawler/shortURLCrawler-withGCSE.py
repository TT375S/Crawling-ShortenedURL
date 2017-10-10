#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import urllib.parse
import re
import sys
import urllib.response
import urllib.request
import urllib.error
import urllib.parse
import json

APIKey = sys.argv[1]
#search from twitter
cx = "008233123352770001943:xjszb8ktj00"

maxPage = 3

try:
    while(1):
        keyword_domainName = input()
        
        for page in range(1,maxPage+1):
            searchApiURL = "https://www.googleapis.com/customsearch/v1?key=" + APIKey + "&cx=" + cx + "&q=" + keyword_domainName + "&hl=ja&start="+ str(page) +"&num=10"
            try:
                with urllib.request.urlopen(urllib.parse.quote_plus(searchApiURL, "/:?=&") ) as response:
                    body = response.read().decode('utf-8') 
                    print(body)
                    #convert array and dictionary
                    resultJson = json.load(body)
                    #checking all items
                    for item in resultJson["items"]:
                        snippet = item["snippet"]
                        #collecting all URL
                        urls = re.findall('(?:https?:\/\/|)'+ keyword_domainName  +'\/[0-9a-zA-Z]*' , snippet)
                        for url in urls:
                            print(url)
                                    
            except urllib.error.HTTPError:
                print("404",file=sys.stderr)
except EOFError:
    pass
