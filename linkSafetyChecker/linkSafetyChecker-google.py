#!/usr/bin/env python
# -*- coding: utf-8 -*-

#TODO: refactoring

import time
import urllib.parse
import re
import sys
import urllib.response
import urllib.request
import urllib.error
import urllib.parse
import json

urlCount = 0
unsafeURLcount = 0

APIKey = sys.argv[1]
method = "POST"
headers = {"Content-Type" : "application/json"}

try:
    while(1):
        
        obj = {
            "client": {
                "clientId":      "yourcompanyname",
                "clientVersion": "1.5.2"
            },
            "threatInfo": {
                "threatTypes":      ["MALWARE", "SOCIAL_ENGINEERING"],
                "platformTypes":    ["WINDOWS"],
                "threatEntryTypes": ["URL"],
                "threatEntries": [
                    #{"url": "http://aaa"},
                    #{"url": "http://bbb"}
                ]
            }
        }

        #Google Safe Brawsing accepts 500 url query per 1 request.
        lineCount = 0
        while lineCount < 500:
            try:
                url = input()
            except EOFError:
                break
            #print(url, file=sys.stderr)
            
            #validation URL form
            if  len(re.findall('(https?:\/\/)[^\s ]+' , url)) <= 0:
                continue
            urlCount += 1
        
            (obj["threatInfo"])["threatEntries"].append({"url": url})
            lineCount += 1


        json_data = json.dumps(obj).encode("utf-8")

        checkerURL = "https://safebrowsing.googleapis.com/v4/threatMatches:find?key=" + APIKey
        request = urllib.request.Request(checkerURL, data=json_data, method=method, headers=headers)
        print("requesting...", file=sys.stderr)
        try:
            with urllib.request.urlopen(request) as response:
                body = response.read().decode('utf-8') 
                #URL is unsafe!!!
                if "threat" in body:
                    print(body)
                    print("threat!", file=sys.stderr)
            if lineCount != 500:
                exit()
        except urllib.error.HTTPError:
            print("404",file=sys.stderr)
except EOFError:
    print(str(urlCount) + " " + str(unsafeURLcount) + " " + str(unsafeURLcount/urlCount), sys.stderr)
    pass

