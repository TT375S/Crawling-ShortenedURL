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

# run chrome headless
options = Options()
options.add_argument('--headless')

# install chromedriver if not found and start chrome
driver = SeleneDriver.wrap(webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=options))

#domain name (NOT FQDN)
targetWord = 'tinyurl.com'

# search 'python' in google
driver.get('https://twitter.com/search?q='+ urllib.parse.quote(targetWord) +'&src=typd')
print('https://twitter.com/search?q='+ urllib.parse.quote(targetWord) +'&src=typd')
#input = driver.find_element_by_name('q')
#input.send_keys('Python')
#input.send_keys(Keys.RETURN)

#show HTML
#print(driver.page_source)

scrollToY = 0
hitCount = 0
for i in range(0, 10):
    #scroll
    #print(driver.page_source)
    driver.execute_script("window.scrollTo(0,"+ str(scrollToY) +")")
    scrollToY += 4000
    time.sleep(1)
    driver.save_screenshot('result_'+ targetWord  + str(i)  +'.png')
    
    urls = re.findall(targetWord + '/[0-9a-zA-Z]+', driver.page_source)
    hitCount += len(urls)
    print(urls)
    print(str(len(urls)) )
#print(driver.page_source)

print("sum:" + str(hitCount) )
# save screen shot
#driver.save_screenshot('result.png')

driver.quit()
