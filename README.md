# Crawling-ShortenedURL
Short URL collection  programs.  
  
For more details, see README.md in each directories of crawler.  
  
# Installation
Need Python3 and selenium, and GoogleChrome for below example.  
## For Mac

Install python3.  
`$ brew install python3`  
  

Install pip3.  
`$ sudo apt install python3-pip`  
  
~~On my Mac, all dependencies are installed by this command.~~  
Install selenium.  
`$ pip3 install selenium`  
  
Install latest version selene.  
`$sudo pip3 install --upgrade selene --pre`  
  
Install Google Chrome.<https://www.google.com/chrome/browser/desktop/index.html>  
  
Clone this repository.  
`$ git clone https://github.com/TT375S/Crawling-ShortenedURL.git`   

## For Ubuntu
Install python3.  
`$ sudo apt install python3`  
Install pip3.  
`$ sudo apt install python3-pip`  
Install latest version selene.  
`$sudo pip3 install --upgrade selene --pre`  
  
Install Google Chrome.<https://www.google.com/chrome/browser/desktop/index.html>  
  
Clone this repository.  
`$ git clone https://github.com/TT375S/Crawling-ShortenedURL.git`   

# Example Usage
Collect short URL from twitter. It collects short URL by scraping twitter search page.  

    $ python3 ./crawler/twitter-crawler/twitterCrawl-allDomain.py < serviceList-domain.txt > shortURLfromTwitter.txt
    https://twitter.com/search?q=tinyurl.com&src=typd
    171
    https://twitter.com/search?q=bit.ly&src=typd
    19
    ...
    

The output file(shortURLfromTwitter.txt) is ...

    $ cat ./crawler/twitter-crawler/shortURLfromTwitter.txt
    Checking for mac64 chromedriver:2.33 in cache
    There is no cached driver. Downloading new one...
    tinyurl.com/yckvuxoq
    tinyurl.com/y7b7fvjl
    tinyurl.com/y82whs2m
    tinyurl.com/ydx4z6sa
    tinyurl.com/yamaqvsg

Then, validate short url and list their destination.

    $ python3 ./linkValidator/linkValidator.py < shortURLfromTwitter.txt > linkDestination.txt
    http://tinyurl.com/yckvuxoq
    http://tinyurl.com/y7b7fvjl
    http://tinyurl.com/y82whs2m
    http://tinyurl.com/ydx4z6sa
    ...

The output file(linkDestination.txt) is ...

    $ cat linkDestination.txt
    https://www.ichibata.co.jp/railway/topics/2017/10/511615511.html
    https://mainichigahakken.net/hobby/article/post-88.php
    http://xn--q9js249txe1ans9a.com/119/
    http://www.rurubu.com/news/detail.aspx?ArticleID=12386
    ...


Finally, check safety of URLs. 

    $ python3 ./linkSafetyChecker/linkSafetyChecker-google.py "YOURAPIKEY" < linkDestination.txt > unsafeList.txt
It's return JSON. (Google API's raw response body)
  
It returns JSON of treat infomation if there are some URL in the input file matches Google's threat URL lists.

