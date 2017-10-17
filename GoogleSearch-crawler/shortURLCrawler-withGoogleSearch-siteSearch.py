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
options.add_argument('--headless')
# install chromedriver if not found and start chrome
driver = SeleneDriver.wrap(webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=options))

domainNames = []
#Input target short url service's domain names.
try:
    while(1):
        domainNames.append(input())
except EOFError:
    pass

for domainName in domainNames:        
    print(domainName, file = sys.stderr)
    shortURLCount = 0
    for page in range(1,maxPage+1):
        searchURL = "https://www.google.co.jp/search?q="+"&client=safari&rls=en&dcr=0&ei=oV_lWbqyD8ip0ATzzoLYBA&start="+ str( 10*(page-1) ) +"&sa=N&biw=973&bih=643&as_sitesearch=" + domainName
        driver.get(searchURL)
        time.sleep(20.0)
                
        html = driver.page_source
        #print(html, file=sys.stderr)
        
        #Converting soup object.
        soup = BeautifulSoup(html, "html.parser")
        searchResults = soup.find_all(class_ = "g")
        
        #Checking each search result items.
        for searchResult in searchResults:
            
            #Finding urls in the search result web site.
            siteDescriptor = (searchResult.find("cite")).string
            linkURL = re.findall('(?:https?:\/\/|)'+ domainName  +'\/[0-9a-zA-Z]+' , siteDescriptor )
            
            if len(linkURL) <1:
                continue
            
            shortURLCount += 1
            print(linkURL[0].replace("https://", "").replace("http://", "") )
        
        if shortURLCount == 0:
            print(html, file = sys.stderr)    
    print(str(shortURLCount), file=sys.stderr)
driver.quit()
