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
#A GoogleCustomSearchEngine(GCSE) whose target site is Twitter.com
#cx = "008233123352770001943:xjszb8ktj00"
#A GCSE whose main target site is github.com but also all of web.
cx = "008233123352770001943:qwfkdxwjxws"

maxPage = 1
maxItems = 10

domainNames = []
try:
    while(1):
        domainNames.append(input())
except EOFError:
    pass

for domainName in domainNames:        
    for page in range(0,maxPage):
        searchApiURL = "https://www.googleapis.com/customsearch/v1?key=" + APIKey + "&cx=" + cx + "&q=" +"site:"+ domainName + "&hl=ja&start="+ str(1+ page * maxItems ) +"&num="+str(maxItems)
        try:
            with urllib.request.urlopen(urllib.parse.quote_plus(searchApiURL, "/:?=&") ) as response:
                body = response.read().decode('utf-8') 
                print(body, file = sys.stderr)
                #convert array and dictionary
                resultJson = json.loads(body)
                #checking all items
                for item in resultJson["items"]:
                    #snippet = item["snippet"]
                    ##collecting all URL
                    #urls = re.findall('(?:https?:\/\/|)'+ domainName  +'\/[0-9a-zA-Z]+' , snippet)
                    #for url in urls:
                    #    print(url.replace("https://", "").replace("http://", "") )
                    
                    print(item["link"].replace("https://", "").replace("http://", "") )

                    #try:    
                    #    #Finding urls in the "item" site.
                    #    with urllib.request.urlopen(urllib.parse.quote_plus(item["link"], "/:?=&") ) as response:
                    #        body = response.read().decode('utf-8') 
                    #        urls = re.findall('(?:https?:\/\/|)'+ domainName  +'\/[0-9a-zA-Z]+' , body)
                    #        for url in urls:
                    #            print(url.replace("https://", "").replace("http://", "") )
                    #
                    #except urllib.error.HTTPError:
                    #    print("404", file=sys.stderr)       
        except urllib.error.HTTPError:
            print("404",file=sys.stderr)
