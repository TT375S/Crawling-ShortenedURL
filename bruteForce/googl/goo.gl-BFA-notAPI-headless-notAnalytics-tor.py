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
#use tor. Before running this script, boot tor service in your computer.
options.add_argument('--proxy-server=socks5://localhost:9050')
#options.add_argument('--host-resolver-rules="MAP * 0.0.0.0 , EXCLUDE localhost"')

def bootBrawser(path):
# install chromedriver if not found and start chrome
    rawDriver = webdriver.Chrome(executable_path=path, chrome_options=options)
    #rawDriver = webdriver.Chrome( chrome_options=options)
    driver = SeleneDriver.wrap(rawDriver)

    driver.set_page_load_timeout(30)
    return (rawDriver, driver)

driverPath =ChromeDriverManager().install() 
(rawDriver, driver) = bootBrawser(driverPath);

for length in range(1, 20):
    #repeated permutation of [0-9a-zA-Z].
    challengeTexts = list(itertools.product(challengeChar, repeat=length) )
    
    prevRetriedChallengeText = challengeTexts[0]
        
    timeoutCount = 0
    for challengeText in challengeTexts:
        url = "http://goo.gl/"+ "".join(challengeText)
        try:
            time.sleep(0.1)
            driver.get(url)
            print(url, file=sys.stderr)
            html = driver.page_source
            
            #detected by robot detection
            if "try again" in html:
                print("DETECTED", file = sys.stderr)
                #reboot brawser
                driver.quit()
                (rawDriver, driver) = bootBrawser(driverPath)
                if not challengeText == prevRetriedChallengeText:
                    #try again
                    challengeTexts.insert(0, challengeText)
                    prevRetriedChallengeText = challengeText
                else:
                    print("Failed retring",file = sys.stderr)
            #The short url is valid!
            elif not "does not exist" in html:
                print("HIT: " + rawDriver.current_url, file = sys.stderr)
                print(url)
                print(rawDriver.current_url, file = sys.stderr)
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
                print("caused by: "+ "".join(challengeText), file = sys.stderr)
                #Reboot headless
                driver.quit()
                (rawDriver, driver) = bootBrawser(driverPath);
                if not challengeText == prevRetriedChallengeText:
                    #try again
                    challengeTexts.insert(0, challengeText)
                    prevRetriedChallengeText = challengeText
                else:
                    print("Failed retring", file = sys.stderr)
                #print("timeout: " + rawDriver.current_url, file = sys.stderr) 
                #print("".join(challengeText))
                #print(rawDriver.current_url)
                continue
            #For rawDriver.current_url . It causes another exception in case of bit.ly don't give any response.
            except:
                 print (traceback.format_exc())  
driver.quit()
