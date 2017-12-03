#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import datetime
#import timedelta
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

#logFileName = "log"+ datetime.datetime.now().strftime('%Y-%m-%d--%H-%M-%S')  +".txt"

maxPage = 100
#weeks
timeRange = 4
#4weeks * 12months * 2years
limitTimeRange = 4 * 12 * 10

# run chrome headless
options = Options()
#options.add_argument('--headless')
#use tor. Before running this script, boot tor service in your computer.
options.add_argument('--proxy-server=socks5://localhost:9050')

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
    
    today = datetime.datetime.now()
    upperLimit = today + datetime.timedelta(weeks=timeRange)
    lowerLimit = today
    limit = today - datetime.timedelta(weeks=limitTimeRange)
    
    print(limit.strftime('%Y/%m/%d') +" ~ "+today.strftime('%Y/%m/%d'), file = sys.stderr)

    #searching  month by month
    while lowerLimit.timestamp() > limit.timestamp(): 
        
        #set search period
        upperLimit = upperLimit - datetime.timedelta(weeks=timeRange)
        lowerLimit = upperLimit - datetime.timedelta(weeks=timeRange)
        print(lowerLimit.strftime('%Y/%m/%d') +" ~ "+upperLimit.strftime('%Y/%m/%d'), file = sys.stderr)

        #specify search period (ex. 2017/01/01 ~ 2017/05/01)
        #It's specified with UNIX time.
        searchPageUrl = "https://search.yahoo.co.jp/search?ei=UTF-8&fl=0&p=aa&vs=" + domainName + "&day_from=" + lowerLimit.strftime('%Y/%m/%d')  + "&day_to=" + upperLimit.strftime('%Y/%m/%d')  + "&fr=top_ga1_sa"

        
        prevUrlCountInThisPage = -1
        for page in range(1,maxPage+1):
            currentSearchPageUrl = searchPageUrl + "&b=" + str(10*(page-1)+1)

            #print(currentSearchPageUrl, file = sys.stderr)
            driver.get(currentSearchPageUrl)
            time.sleep(2.0)

            #driver.save_screenshot('result_'+ domainName +"_"  + str(page)  +'.png')        
            html = driver.page_source
            #print(html, file=sys.stderr)

            #Converting soup object.
            soup = BeautifulSoup(html, "html.parser")
            searchResults = soup.find_all(class_ = "hd")
            
            urlCountInThisPage = 0
            #Checking each search result items.
            for searchResult in searchResults:
                
                #Finding urls in the search result web site.
                siteDescriptor = (searchResult.find("a") ).get("href")
                linkURL = re.findall('(?:https?:\/\/|)'+ domainName  +'\/[0-9a-zA-Z]+' , siteDescriptor )
                
                if len(linkURL) <1:
                    continue
                
                urlCountInThisPage += 1
                urlCount += 1
                print(linkURL[0].replace("https://", "").replace("http://", "") )
            
            #Result is empty.
            if urlCountInThisPage == 0:
                break
            #Result is empty(SearchPage somtimes returns same page to different page number.)
            if prevUrlCountInThisPage == urlCountInThisPage and not urlCountInThisPage == 10:
                break
            prevUrlCountInThisPage = urlCountInThisPage
        print(str(urlCount), file = sys.stderr)
driver.quit()
