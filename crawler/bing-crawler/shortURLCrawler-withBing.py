#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import urllib.parse
import re
import sys
import urllib.response
import urllib.request
import urllib.error
import urllib.parse
import json

from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selene.driver import SeleneDriver
from webdriver_manager.chrome import ChromeDriverManager

from bs4 import BeautifulSoup

maxPage = 10

# run chrome headless
options = Options()
#options.add_argument('--headless')
# install chromedriver if not found and start chrome
rawDriver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=options)
driver = SeleneDriver.wrap(rawDriver)


domainNames = []
#Input target short url service's domain names.
try:
    while(1):
        domainNames.append(input())
except EOFError:
    pass

for domainName in domainNames:
    urlCount = 0        
    print(domainName, file = sys.stderr)
    
    bingURL = "http://www.bing.com"
    driver.get(bingURL)
    time.sleep(2)
    #print(rawDriver.current_url)

    #Enter keyword and search.
    input_element = driver.find_element_by_name('q')
    input_element.send_keys(domainName)
    input_element.send_keys(Keys.RETURN)
   
    time.sleep(2) 
    searchPageUrl = rawDriver.current_url

    for page in range(1,maxPage+1):
        currentSearchPageUrl = searchPageUrl + "&start=" + str(10*(page-1))

        #print(searchURL, file = sys.stderr)
        driver.get(currentSearchPageUrl)
        time.sleep(3.0)

        #driver.save_screenshot('result_'+ domainName +"_"  + str(page)  +'.png')        
        html = driver.page_source
        #print(html, file=sys.stderr)
        
        #Converting soup object.
        soup = BeautifulSoup(html, "html.parser")
        searchResults = soup.find_all(class_ = "b_algo")

        urlCountInThisPage = 0
        #Checking each search result items.
        for searchResult in searchResults:
            #Finding urls in the search result web site.
            linkURL = (searchResult.find("a")).get("href")
            print(linkURL.replace("https://", "").replace("http://", "") )
            urlCount += 1
            urlCountInThisPage += 1

        if urlCountInThisPage == 0:
            break
    print(str(urlCount), file = sys.stderr)
driver.quit()
