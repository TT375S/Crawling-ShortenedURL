# Crawling-ShortenedURL
Crawling twitter, github, etc… and collection short URL.

For more details, see README.md in each directories of crawler.  

# Example Usage
Collect short URL from twitter.  
    $ python3 ./twitter-crawler/twitterCrawl-allDomain.py < serviceList-domain.txt > shortURLfromTwitter.txt
    https://twitter.com/search?q=tinyurl.com&src=typd
    171
    https://twitter.com/search?q=bit.ly&src=typd
    19
    ...

The output file(shortURLfromTwitter.txt) is ...

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
    https://www.ichibata.co.jp/railway/topics/2017/10/511615511.html
    https://mainichigahakken.net/hobby/article/post-88.php
    http://xn--q9js249txe1ans9a.com/119/
    http://www.rurubu.com/news/detail.aspx?ArticleID=12386
    ...

Finally, check safety.
    $ python3 ./linkSafetyChecker/linkSafetyChecker-google.py "YOURAPIKEY" < linkDestination.txt > unsafeList.txt
It's return JSON. (Google API's raw response body)


