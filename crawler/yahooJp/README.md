# short URL collector from Baidu
This program collects short url with Baidu search.

## Installation
It needs Python3, GoogleChrome, selene and BeautifulSoup.

## Usage
`python3 shortURLCrawler-yahoo-timeSpecified.py < ../service-domain.txt > res.txt`  
Then, remove duplication.  
`sort res.txt | uniq`

## In japanese...
検索結果ページをスクレイピングするならYahoo.co.jpが一番良い感じ。  
検索キーワードに空白が指定できないのが残念。  

