#!/usr/bin/env python
# -*- coding: utf-8 -*-

import traceback
import time
import urllib.parse
import re
import sys
import urllib.response
#import urllib.request
import urllib.error
import urllib.parse

from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selene.driver import SeleneDriver
from webdriver_manager.chrome import ChromeDriverManager

validURLcount = 0
urlCount = 0
_404count = 0

# run chrome headless
options = Options()
options.add_argument('--headless')
#use tor. Before running this script, boot tor service in your computer.
options.add_argument('--proxy-server=socks5://localhost:9050')

# install chromedriver if not found and start chrome
rawDriver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=options)
driver = SeleneDriver.wrap(rawDriver)


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

        #request
        try:
            driver.get(url)
        except KeyboardInterrupt:
            print (traceback.format_exc())
            break
        except:
            print (traceback.format_exc())
            print(url, file=sys.stderr)
            pass
        else:
            print(rawDriver.current_url)
            validURLcount += 1

except EOFError:
    pass

print(str(urlCount) + " " + str(validURLcount) + " " + str(_404count), sys.stderr)
