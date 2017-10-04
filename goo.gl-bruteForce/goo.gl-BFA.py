# -*- coding: utf-8 -*-

import urllib.parse
import urllib.request
import urllib.error
import re
import sys
import time
import itertools
import string

from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selene.driver import SeleneDriver
from webdriver_manager.chrome import ChromeDriverManager

challengeChar = []
for i in range(0,10):
    challengeChar.append(str(i))
for i in string.ascii_lowercase[:26]:
    challengeChar.append(i)
for i in string.ascii_uppercase[:26]:
    challengeChar.append(i)
    
# run chrome headless
options = Options()
options.add_argument('--headless')

# install chromedriver if not found and start chrome
driver = SeleneDriver.wrap(webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=options))

for length in range(3, 10):
    #repeated permutation of [0-9a-zA-Z].
    challengeTexts = list(itertools.product(challengeChar, repeat=length) )

    #print(challengeTexts)
    for challengeText in challengeTexts:
        #url = "http://goo.gl/" + "".join(challengeText) +"+"
        url = "https://goo.gl/#analytics/goo.gl/"+ "".join(challengeText) +"/all_time"
        driver.get(url)
        print(url, file=sys.stderr)
        html = driver.page_source
        
        #If length of response is greater than 200,000 characters, it means succeeded!
        if len(html) > 200000:
            print("".join(challengeText))
            print("HIT", sys.stderr)
        #print(html)
        #print(url)
        #Avoid "Too many request" error.
        time.sleep(0.05)
driver.quit()
