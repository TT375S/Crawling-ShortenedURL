# -*- coding: utf-8 -*-
import traceback
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
from selenium.common.exceptions import TimeoutException
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
#options.add_argument('--headless')
#disable image loading
options.add_argument('--blink-settings=imagesEnabled=false')

# install chromedriver if not found and start chrome
rawDriver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=options)
driver = SeleneDriver.wrap(rawDriver)

driver.set_page_load_timeout(10)

for length in range(2, 10):
    #repeated permutation of [0-9a-zA-Z].
    challengeTexts = list(itertools.product(challengeChar, repeat=length) )
    
    timeoutCount = 0
    for challengeText in challengeTexts:
        url = "http://bit.ly/"+ "".join(challengeText)
        try:
            time.sleep(0.1)
            driver.get(url)
            print(url, file=sys.stderr)
            html = driver.page_source
            
            #The short url is valid!
            if not "does not exist" in html:
                print("HIT: " + rawDriver.current_url, file = sys.stderr)
                print("".join(challengeText))
                print(rawDriver.current_url)
        except TimeoutException:
            timeoutCount += 1
            try:
                print("timeout: " + str(timeoutCount), file=sys.stderr)
                print("caused by: "+ "".join(challengeText))
                #print("timeout: " + rawDriver.current_url, file = sys.stderr) 
                #print("".join(challengeText))
                #print(rawDriver.current_url)
                continue
            #For rawDriver.current_url . It causes another exception in case of bit.ly don't give any response.
            except:
                 print (traceback.format_exc())  
driver.quit()
