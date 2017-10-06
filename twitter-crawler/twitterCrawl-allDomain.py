#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selene.driver import SeleneDriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import urllib.parse
import re
import sys

# run chrome headless
options = Options()
options.add_argument('--headless')
# install chromedriver if not found and start chrome
driver = SeleneDriver.wrap(webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=options))

try:
    while(1):
        #domain name (NOT FQDN)
        targetWord = input()

        url = 'https://twitter.com/search?q='+ urllib.parse.quote(targetWord) +'&src=typd' 
        driver.get(url)
        print(url, file=sys.stderr)

        #twitter search screen can be scrolled limitelessly.
        scrollToY = 0
        hitCount = 0
        for i in range(0, 20):
            #scroll
            driver.execute_script("window.scrollTo(0,"+ str(scrollToY) +")")
            scrollToY += 4000
            #wait loading
            time.sleep(1)
            driver.save_screenshot('result_'+ targetWord  + str(i)  +'.png')
            
        #print(driver.page_source)

        #search short URLs
        urls = re.findall(targetWord + '/[0-9a-zA-Z]+', driver.page_source)
        stripDupUrls = set(urls)
        hitCount += len(urls)
        for url  in stripDupUrls:
            print(url)
        print( len(stripDupUrls) ,file=sys.stderr )
        
        # save screen shot
        #driver.save_screenshot('result.png')
except EOFError:
    pass
driver.quit()
