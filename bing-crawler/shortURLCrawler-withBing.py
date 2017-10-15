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

#https://qiita.com/zarchis/items/3258562ebc9570fa05a3
def conv_encoding(data):
    lookup = ('utf_8', 'euc_jp', 'euc_jis_2004', 'euc_jisx0213',
              'shift_jis', 'shift_jis_2004','shift_jisx0213',
              'iso2022jp', 'iso2022_jp_1', 'iso2022_jp_2', 'iso2022_jp_3',
              'iso2022_jp_ext','latin_1', 'ascii')
    encode = None
    for encoding in lookup:
        try:
            data = data.decode(encoding)
            encode = encoding
            break
        except:
            pass
        if isinstance(data, unicode):
            return data,encode
    else:
        raise LookupError

maxPage = 1
maxItems = 10
targetSite = "github.com"

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
    for page in range(1,maxPage+1):
        #time.sleep(1)
        searchURL = "http://www.bing.com/search?q=%28site%3A"+targetSite+"%29+"+domainName+"&go=検索&qs=n&form=QBRE&filt=all&sp=-1&pq=%28site%3A"+targetSite+"%29+"+domainName+"&sc=0-24&sk=&cvid=71DD0548CAEF4EE2A40147845017D076"

        driver.get(searchURL)
        time.sleep(1.0)
                
        html = driver.page_source
        #print(html, file=sys.stderr)
        
        #Converting soup object.
        soup = BeautifulSoup(html, "html.parser")
        searchResults = soup.find_all(class_ = "b_algo")

        #Checking each search result items.
        for searchResult in searchResults:
            #Checking snippet
            snippet = (searchResult.find("p") ).string
            #print(snippet)
            urls = re.findall('(?:https?:\/\/|)'+ domainName  +'\/[0-9a-zA-Z]+' , html )
            for url in urls:
                print(url.replace("https://", "").replace("http://", "") )
            
            #Finding urls in the search result web site.
            linkURL = (searchResult.find("a")).get("href")
            print(linkURL, file=sys.stderr)
           
            driver.get(linkURL)
            time.sleep(1)
            
            #body,encoding = conv_encoding(response.read() )
            body = driver.page_source
            
            urls = re.findall('(?:https?:\/\/|)'+ domainName  +'\/[0-9a-zA-Z]+' , body )
            for url in urls:
                print(url.replace("https://", "").replace("http://", "") )
driver.quit()
