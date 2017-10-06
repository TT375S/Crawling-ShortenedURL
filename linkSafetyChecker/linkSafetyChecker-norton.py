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

urlCount = 0
unsafeURLcount = 0

try:
    while(1):
        url = input()
        print(url, file=sys.stderr)
        #validation URL form
        if  len(re.findall('(https?:\/\/)[^\s ]+' , url)) <= 0:
            continue

        urlCount += 1

        checkerURL = "https://safeweb.norton.com/report/show?url=" + urllib.parse.quote_plus(url, "/:?=&") 

        try:
            with urllib.request.urlopen(urllib.parse.quote_plus(checkerURL, "/:?=&")) as response:
                html = response.read().decode('utf-8') 
                #print(html)
                if "big_clip icoSafe" in html:
                    print("SAFE", file=sys.stderr)
                elif "big_clip icoUntested" in html:
                    print("UNTESTED", file=sys.stderr)
                else:
                    unsafeURLcount += 1
                    print("UNSAFE", file=sys.stderr)
                    print(url)
        except urllib.error.HTTPError:
            print("404",file=sys.stderr)
except EOFError:
    pass

print(str(urlCount) + " " + str(unsafeURLcount) + " " + str(unsafeURLcount/urlCount), sys.stderr)
