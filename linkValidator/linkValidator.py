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

validURLcount = 0
urlCount = 0

try:
    while(1):
        url = "http://" + input()
        print(url, file=sys.stderr)
        #validation URL form
        if  len(re.findall('(?:https?:\/\/|)[^\s ]+\/[0-9a-zA-Z]*' , url)) <= 0:
            continue

        urlCount += 1

        try:
            with urllib.request.urlopen(urllib.parse.quote_plus(url, "/:?=&")) as response:
                #html = response.read().decode('utf-8') 
                print(response.geturl())
                validURLcount += 1
        except urllib.error.HTTPError:
            print("404")
except EOFError:
    pass

print(str(urlCount) + " " + str(validURLcount) + " " + str(validURLcount/urlCount), sys.stderr)
