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
options.add_argument('--headless')

#!!!!Some of dynamic web app won't work well with this option. It should be disabled!!!!
#disable image loading
#options.add_argument('--blink-settings=imagesEnabled=false')

#use tor. Before running this script, boot tor service in your computer.
#options.add_argument('--proxy-server=socks5://localhost:9050')

#options.add_argument('--host-resolver-rules="MAP * 0.0.0.0 , EXCLUDE localhost"')

driverPath = "2"

def bootBrawser(path):
# install chromedriver if not found and start chrome
    rawDriver = webdriver.Chrome(executable_path=path, chrome_options=options)
    driver = SeleneDriver.wrap(rawDriver)

    driver.set_page_load_timeout(30)
    return (rawDriver, driver)

driverPath = ChromeDriverManager().install()
(rawDriver, driver) = bootBrawser(driverPath);

skip_to_textTuple = ()

#skip
if len(sys.argv) >= 4:
    skip_to_text = sys.argv[3]
    for char in skip_to_text:
        skip_to_textTuple += (char,)
    print(skip_to_textTuple)


for length in range(len("".join(skip_to_textTuple)), 20):
    #repeated permutation of [0-9a-zA-Z].
    challengeTexts = list(itertools.product(challengeChar, repeat=length) )
    #skip to the permutation
    if length == len("".join(skip_to_textTuple)):
        skip_to_index = challengeTexts.index(skip_to_textTuple)
        del challengeTexts[0:skip_to_index]
        print("skip to: " + "".join(skip_to_textTuple) + " at index:" + str(skip_to_index), file = sys.stderr)
    timeoutCount = 0
    for challengeText in challengeTexts:
  
        url = "http://bit.ly/"+ "".join(challengeText)
        try:
            time.sleep(0.1)
            try:
                driver.get(url)
                print(url, file=sys.stderr)
                html = driver.page_source
            except:
                print(traceback.format_exc()) 
            #The short url is valid!
            if not "does not exist" in html:
                print("HIT: " + rawDriver.current_url, file = sys.stderr)
                print("".join(challengeText))
                print(rawDriver.current_url)
                #destination URL
                if len(sys.argv) >= 2:
                    f = open(sys.argv[1], "a")
                    f.write(rawDriver.current_url+"\n")
                    f.close()
                    #short URL hit
                    if len(sys.argv) >= 3:
                        f = open(sys.argv[2], "a")
                        f.write(url+"\n")
                        f.close()
        except TimeoutException:
            timeoutCount += 1
            try:
                print("timeout: " + str(timeoutCount), file=sys.stderr)
                print("caused by: "+ "".join(challengeText))
                #Reboot headless
                driver.quit()
                (rawDriver, driver) = bootBrawser(driverPath);
                #print("timeout: " + rawDriver.current_url, file = sys.stderr) 
                #print("".join(challengeText))
                #print(rawDriver.current_url)
                continue
            #For rawDriver.current_url . It causes another exception in case of bit.ly don't give any response.
            except:
                 print (traceback.format_exc())  
driver.quit()
