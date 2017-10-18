# short URL collector from Baidu
This program collects short url with Baidu search.

## Installation
It needs Python3, GoogleChrome, selene and BeautifulSoup.

## Usage
`python3 shortURLCrawler-withBaidu.py < ../service-domain.txt > res.txt`  
Then, remove duplication.  
`sort res.txt | uniq`

## In japanese...
Baiduはクローリングするドメインを制限しているのか、goo.glなどクローリングしていないドメインがいくつかある。  
それ以外ならちゃんと結果を返すしロボットががんがんアクセスしても注意されない。  
なかなか便利。


