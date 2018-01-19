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

requestCount = 0

while(1):
    
    obj = {
        "client": {
            "clientId":      "yourcompanyname",
            "clientVersion": "1.5.2"
        },
        "threatInfo": {
            "threatTypes":      ["MALWARE", "SOCIAL_ENGINEERING", "THREAT_TYPE_UNSPECIFIED", "UNWANTED_SOFTWARE", "POTENTIALLY_HARMFUL_APPLICATION"],
            "platformTypes":    ["WINDOWS", "PLATFORM_TYPE_UNSPECIFIED", "LINUX", "ANDROID", "OSX", "IOS", "CHROME"],
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
    requestCount += 1
    try:
        with urllib.request.urlopen(request) as response:
            body = response.read().decode('utf-8') 
            #URL is unsafe!!!
            if "threat" in body:
                if requestCount == 1:
                    print(body[0:len(body)-1 -5])
                else:
                    #concatenate json
                    print(",")
                    print(body[4 + 12:len(body)-1 -5])
                
                print("threat!", file=sys.stderr)
        if lineCount != 500:
            #terminate json
            if requestCount != 0:
                print("] }")
            exit()
    except urllib.error.HTTPError:
        print("404",file=sys.stderr)

#except EOFError:
#    print(str(urlCount) + " " + str(unsafeURLcount) + " " + str(unsafeURLcount/urlCount), sys.stderr)
#    pass

