#!/usr/bin/env python
# -*- coding: utf-8 -*-
import traceback
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
_404count = 0

try:
    while(1):
        domain = input()
        #validation URL form
        if  len(re.findall('(?:https?:\/\/|)[^\s ]+\/[0-9a-zA-Z]*' , domain)) <= 0:
            continue
        if "://" in domain:
            url = domain
        else :
            url = "http://" + domain
        #print(url, file=sys.stderr)

        urlCount += 1

        req = urllib.request.Request(
            url, 
            data=None, 
            headers={
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
            }
        )

        #request
        try:
            with urllib.request.urlopen(req) as response:
                print(response.geturl())
                validURLcount += 1
        except urllib.error.HTTPError:
            print("404")
            _404count += 1
        except urllib.error.URLError:
            print (traceback.format_exc())
            pass
        except KeyboardInterrupt:
            print (traceback.format_exc())
            break
        except:
            print (traceback.format_exc())
            print(url, file=sys.stderr)
            pass
        
except EOFError:
    pass

print(str(urlCount) + " " + str(validURLcount) + " " + str(_404count), sys.stderr)
