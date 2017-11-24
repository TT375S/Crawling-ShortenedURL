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

import domainSpecific

from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selene.driver import SeleneDriver
from webdriver_manager.chrome import ChromeDriverManager

class BruteforceDriver:
    def bootBrawser(self, path):
        rawDriver = webdriver.Chrome(executable_path=path, chrome_options=self.options)
        driver = SeleneDriver.wrap(rawDriver)
        
        #set timeout time
        driver.set_page_load_timeout(30)
        return (rawDriver, driver)
    
    def __init__(self, agent):
        self.domainAgent = agent
        self.challengeChar = []
        for i in range(0,10):
            self.challengeChar.append(str(i))
        for i in string.ascii_lowercase[:26]:
            self.challengeChar.append(i)
        for i in string.ascii_uppercase[:26]:
            self.challengeChar.append(i)

        self.logFileData = datetime.datetime.now().strftime('%Y-%m-%d--%H-%M-%S')

        self.options = Options()
        self.options.add_argument('--headless')

        #!!!!Some of dynamic web app won't work well with this option. It should be disabled!!!!
        #disable image loading
        #options.add_argument('--blink-settings=imagesEnabled=false')

        #use tor. Before running this script, boot tor service in your computer.
        #options.add_argument('--proxy-server=socks5://localhost:9050')

        #options.add_argument('--host-resolver-rules="MAP * 0.0.0.0 , EXCLUDE localhost"')
        self.driverPath = ""
        # install chromedriver if not found and start chrome
        self.driverPath = ChromeDriverManager().install()
        (self.rawDriver, self.driver) = self.bootBrawser(self.driverPath);
        self.skip_to_textTuple = ()

    def writeUrls(self, destUrl, shortUrl):
        if len(sys.argv) >= 2:
            f = open(sys.argv[1], "a")
            f.write(destUrl+"\n")
            f.close()
            #short URL hit
            if len(sys.argv) >= 3:
                f = open(sys.argv[2], "a")
                f.write(shortUrl+"\n")
                f.close()



    def main(self):
        #skip
        if len(sys.argv) >= 4:
            skip_to_text = sys.argv[3]
            for char in skip_to_text:
                self.skip_to_textTuple += (char,)
            print(self.skip_to_textTuple)


        for length in range(len("".join(self.skip_to_textTuple)), 20):
            #repeated permutation of [0-9a-zA-Z].
            challengeTexts = list(itertools.product(self.challengeChar, repeat=length) )
            
            prevRetriedChallengeText = challengeTexts[0]
            
            #skip researched pattern (specified by CLI argument)
            if length == len("".join(self.skip_to_textTuple)):
                skip_to_index = challengeTexts.index(self.skip_to_textTuple)
                del challengeTexts[0:skip_to_index]
                print("skip to: " + "".join(self.skip_to_textTuple) + " at index:" + str(skip_to_index), file = sys.stderr)
            
            timeoutCount = 0
            for challengeText in challengeTexts:
                print("".join(challengeText), file = sys.stderr)
                
                url = self.domainAgent.url + "".join(challengeText)
                try:
                    self.driver.get(url)
                    print(url, file=sys.stderr)
                    html = self.driver.page_source
                    
                    #The short url is valid!
                    if self.domainAgent.isValid(url, self.rawDriver.current_url, html):
                        print("HIT: " + self.rawDriver.current_url, file = sys.stderr)
                        print("".join(challengeText))
                        print(self.rawDriver.current_url)
                        self.writeUrls(self.rawDriver.current_url, url)
                except TimeoutException:
                    timeoutCount += 1
                    
                    print("timeout: " + str(timeoutCount), file=sys.stderr)
                    print("caused by: "+ "".join(challengeText), file = sys.stderr)
                    
                    #log url cause timeout
                    f = open("timeOutURL" + self.logFileData + ".txt", "a")
                    f.write(url+"\n")
                    f.close()
                    
                    #Reboot headless
                    self.driver.quit()
                    (self.rawDriver, self.driver) = self.bootBrawser(self.driverPath);
                    
                    #Retry
                    if not challengeText == prevRetriedChallengeText:
                        #try again
                        challengeTexts.insert(0, challengeText)
                        prevRetriedChallengeText = challengeText
                    else:
                        print("Failed retring", file = sys.stderr)
                    continue
                except KeyboardInterrupt:
                    exit()
                except :
                    print(traceback.format_exc())
                    #Reboot headless
                    self.driver.quit()
                    (self.rawDriver, self.driver) = self.bootBrawser(self.driverPath);
                    
                    f = open("exceptionURL" + self.logFileData + ".txt", "a")
                    f.write(url+"\n")
                    f.close()
                    continue
        self.driver.quit()

if __name__ == '__main__':

    domainAgent_class = getattr(domainSpecific, "owly")
    domainAgent = domainAgent_class()

    mainDriver = BruteforceDriver(domainAgent)
    mainDriver.main()
