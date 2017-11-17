# -*- coding: utf-8 -*-
import datetime
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

logFileData = datetime.datetime.now().strftime('%Y-%m-%d--%H-%M-%S')

# run chrome headless
options = Options()
options.add_argument('--headless')

#!!!!Some of dynamic web app won't work well with this option. It should be disabled!!!!
#disable image loading
#options.add_argument('--blink-settings=imagesEnabled=false')

#use tor. Before running this script, boot tor service in your computer.
options.add_argument('--proxy-server=socks5://localhost:9050')

#options.add_argument('--host-resolver-rules="MAP * 0.0.0.0 , EXCLUDE localhost"')

def writeUrls(destUrl, shortUrl):
    #destination URL
    if len(sys.argv) >= 2:
        f = open(sys.argv[1], "a")
        f.write(destUrl+"\n")
        f.close()
        #short URL hit
        if len(sys.argv) >= 3:
            f = open(sys.argv[2], "a")
            f.write(shortUrl+"\n")
            f.close()

driverPath = ""
def bootBrawser(path):
    rawDriver = webdriver.Chrome(executable_path=path, chrome_options=options)
    driver = SeleneDriver.wrap(rawDriver)
    
    #set timeout time
    driver.set_page_load_timeout(30)
    return (rawDriver, driver)

# install chromedriver if not found and start chrome
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
    
    prevRetriedChallengeText = challengeTexts[0]
    
    #skip researched pattern (specified by CLI argument)
    if length == len("".join(skip_to_textTuple)):
        skip_to_index = challengeTexts.index(skip_to_textTuple)
        del challengeTexts[0:skip_to_index]
        print("skip to: " + "".join(skip_to_textTuple) + " at index:" + str(skip_to_index), file = sys.stderr)
    
    timeoutCount = 0
    for challengeText in challengeTexts:
        print("".join(challengeText), file = sys.stderr)
        
        url = "http://ow.ly/"+ "".join(challengeText)
        try:
            driver.get(url)
            print(url, file=sys.stderr)
            html = driver.page_source
            
            #The short url is valid!
            if not destinationUrl == "http://ow.li":
                print("HIT: " + rawDriver.current_url, file = sys.stderr)
                print("".join(challengeText))
                print(rawDriver.current_url)
                writeUrls(rawDriver.current_url, url)
        except TimeoutException:
            timeoutCount += 1
            
            print("timeout: " + str(timeoutCount), file=sys.stderr)
            print("caused by: "+ "".join(challengeText), file = sys.stderr)
            #            try:
            #                current_url = rawDriver.current_url
            #            except TimeoutException:
            #                print(traceback.format_exc())
            #            else:
            #                print(current_url, file = sys.stderr)
            #                if "://" in current_url:
            #                    writeUrls(current_url, url)
            
            #log url cause timeout
            f = open("timeOutURL" + logFileData + ".txt", "a")
            f.write(url+"\n")
            f.close()
            
            #Reboot headless
            driver.quit()
            (rawDriver, driver) = bootBrawser(driverPath);
            
            #Retry
            if not challengeText == prevRetriedChallengeText:
                #try again
                challengeTexts.insert(0, challengeText)
                prevRetriedChallengeText = challengeText
            else:
                print("Failed retring", file = sys.stderr)
            continue
        except :
            print(traceback.format_exc())
            #Reboot headless
            driver.quit()
            (rawDriver, driver) = bootBrawser(driverPath);
            continue

driver.quit()

