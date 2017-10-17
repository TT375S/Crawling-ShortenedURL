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
        searchURL = "https://www.google.co.jp/search?q="+ domainName +"/"+"&client=safari&rls=en&dcr=0&ei=oV_lWbqyD8ip0ATzzoLYBA&start="+ str( 10*(page-1) ) +"&sa=N&biw=973&bih=643&as_sitesearch=" + targetSite
        driver.get(searchURL)
        time.sleep(1.0)
                
        html = driver.page_source
        #print(html, file=sys.stderr)
        
        #Converting soup object.
        soup = BeautifulSoup(html, "html.parser")
        searchResults = soup.find_all(class_ = "g")

        #Checking each search result items.
        for searchResult in searchResults:
            #Checking snippet
            #これはいらん理由は以下
            #Googleは検索結果のスニペットでキーワードと一致している部分を<em>タグで囲んで強調文字にする
            #そのためタグをstripしないと文字列の検索が正しくできない
            #(英語でコメント書くのめんどくさい)
            #snippet = (searchResult.find(class_ ="st") ).string
            #print(snippet)
            #urls = re.findall('(?:https?:\/\/|)'+ domainName  +'\/[0-9a-zA-Z]+' , html )
            #for url in urls:
            #    print(url.replace("https://", "").replace("http://", "") )
            
            #Finding urls in the search result web site.
            linkURL = (searchResult.find("a")).get("href")
            print(linkURL, file=sys.stderr)
           
            driver.get(linkURL)
            #Time for web page loading and javascript rendering
            time.sleep(0.5)
            
            body = driver.page_source
            
            urls = re.findall('(?:https?:\/\/|)'+ domainName  +'\/[0-9a-zA-Z]+' , body )
            for url in urls:
                print(url.replace("https://", "").replace("http://", "") )
driver.quit()
