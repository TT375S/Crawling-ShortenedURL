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

searchType = ["Code", "Commits", "Issues", "Wikis", "Users"]

try:
    while(1):
        #domain name (NOT FQDN)
        targetShortURLDomain = input()
        
        #Github can search Code, Commits, Issues, etc...
        for stype in searchType:
            #Page number of search screen.
            for pageNum in range(1, 2):
                url = "http://github.com/search?p="+str(pageNum)+"&utf8=✓&q="+targetShortURLDomain+"&type=" + stype
                driver.get(url)
                
                #Github abuse detection is very strict.
                time.sleep(10)

                print(url, file=sys.stderr)
                #print(driver.page_source)
                driver.save_screenshot('result_'+ targetShortURLDomain +"_"+stype  + str(pageNum)  +'.png')

                shortURLs = re.findall(targetShortURLDomain +'(?:</em>|)'+'/[0-9a-zA-Z]+', driver.page_source)
                nodup = set(shortURLs)
                print(len(shortURLs), file=sys.stderr)
                for url  in nodup:
                    print(url.replace('</em>',''))
except EOFError:
    pass
driver.quit()
