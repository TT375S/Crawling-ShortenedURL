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

maxPage = 10
#weeks
timeRange = 8
#4weeks * 12months * 2years
limitTimeRange = 4 * 12 * 2

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
    
    baiduURL = "http://www.baidu.com"
    driver.get(baiduURL)
    time.sleep(2)
    #print(rawDriver.current_url)

    #Enter keyword and search.
    input_element = driver.find_element_by_name('wd')
    input_element.send_keys("site:("+domainName + ")")
    input_element.send_keys(Keys.RETURN)
   
    time.sleep(2) 
    searchPageUrl = rawDriver.current_url
    
    parsedURL = urllib.parse.urlparse(searchPageUrl)
    parsedQuery = urllib.parse.parse_qs(parsedURL.query)
    
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

        #specify search period (ex. 2017/01/01 ~ 2017/05/01)
        #It's specified with UNIX time.
        parsedQuery["gpc"] = "stf="+ str(round(lowerLimit.timestamp()) ) +","+ str(round(upperLimit.timestamp()) ) +"|stftype=2"
    
        #In baidu, I don't know why but keyword is surrounded by "[" and "]"
        parsedQuery["wd"] = "site:(" + domainName + ")"

        queryString = urllib.parse.urlencode(parsedQuery)
        parts = (parsedURL.scheme, parsedURL.netloc, parsedURL.path, parsedURL.params, queryString, parsedURL.fragment)    

        searchPageUrl = urllib.parse.urlunparse(parts)
        #print(searchPageUrl, file = sys.stderr)
        
        
        prevUrlCountInThisPage = -1
        for page in range(1,maxPage+1):
            currentSearchPageUrl = searchPageUrl + "&pn=" + str(10*(page-1))

            #print(currentSearchPageUrl, file = sys.stderr)
            driver.get(currentSearchPageUrl)
            time.sleep(2.0)

            #driver.save_screenshot('result_'+ domainName +"_"  + str(page)  +'.png')        
            html = driver.page_source
            #print(html, file=sys.stderr)

            #Converting soup object.
            soup = BeautifulSoup(html, "html.parser")
            searchResults = soup.find_all(class_ = "result c-container ")
            
            urlCountInThisPage = 0
            #Checking each search result items.
            for searchResult in searchResults:
                
                #Finding urls in the search result web site.
                siteDescriptor = (searchResult.find(class_ = "c-showurl") ).string
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
