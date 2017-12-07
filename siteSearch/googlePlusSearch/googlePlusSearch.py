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

def writeFile(fileName, mode, text):
    f = open(fileName, mode)
    f.write(text+"\n")
    f.close()

unsafeURLcount = 0

APIKey = sys.argv[1]


keyword = "bit.ly"

nextPageToken = ""
urlCount = 0
for i in range(100):
    checkerURL = "https://www.googleapis.com/plus/v1/activities?query="+keyword+"&key=" + APIKey
    if len(nextPageToken) >= 1:
        checkerURL += "&pageToken="+nextPageToken
    request = urllib.request.Request(checkerURL)
    try:
        with urllib.request.urlopen(request) as response:
            body = response.read().decode('utf-8') 
            #print(body, file=sys.stderr)
            writeFile("logSTDERR"+".txt", "a", body)

            jsonData = json.loads(body)
            nextPageToken = jsonData["nextPageToken"]
            print("next: "+nextPageToken, file=sys.stderr)
            print(str(urlCount), file=sys.stderr)
            items = jsonData["items"]
            for item in items:
                title = item["title"]
                
                #remove HTML tags
                p = re.compile(r"<[^>]*?>")
                content = p.sub("", item["object"]["content"])  

                
                linkURLs = re.findall('(?:https?:\/\/|)'+ keyword  +'\/[0-9a-zA-Z]+' , title + " " + content )
                for linkURL in linkURLs:
                    urlCount += 1
                    print(linkURL)
    except urllib.error.HTTPError:
        print("404",file=sys.stderr)
