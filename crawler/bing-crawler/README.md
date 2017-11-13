# short URL collector from Bing
This program collects short url by the Bing Search.  
Without the Bing API, it merely scrapes the Bing search results page.  
Default setting is that target web site is the github.com.

## Installationa
Need Python3, selen, GoogleChrome, BeautifulSoup.
 
## Usage
`$ python3 shortURLCrawler-withBing.py < ../serviceList-domain.txt > result.txt`

## In japanese... 
13分で150個（重複除く)。sleepしてる時間を削ればもっと早くなるし、人気のない短縮URLサービスを検索候補から外せば良い。  
なおgithub.com内の検索。サイト指定なしで検索するとあまり引っかからなかったので。



