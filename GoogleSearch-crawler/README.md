# short URL collector from Google Custom Search
A program collects short URL with Google Search / Google custom search API.

### shortURLCrawler-withGCSE.py
Input short URL service's domain names. They are listed in "serviceList-domain.txt". So, input the file with redirection.  
Then, this program search by the domain names with GoogleCustomSearch.  
It requests only first 1 page of the search results in order to saving number of request times. (GoogleCustomSearch restricts free accounts  number of request times.)  
Then it visits each web sites in search results, ans lists up short urls. The search objects are all items in a given service domain name lists such that "serviceList-domain.txt". 

### shortURLCrawler-withGoogleSearch.py
It has basicaly same function with "shortURLCrawler-withGCSE.py".  
The difference is this program using Google Search but Google custom search API.  


## Installation
Need python3.  

### shortURLCrawler-withGoogleSearch.py
In addition, it need GoogleChrome, selene and BeautifulSoup. 


## Usage
`$ pyhton3 ./GoogleSearch-crawler/shortURLCrawler-withGCSE.py < ../serviceList-domain.txt > result.txt`  
The result.txt contains so many duplications. Then, remove them.  
`$ sort result.txt | uniq`  

## In japanese... 
  
検索したい短縮URLサービスのドメイン、bit.lyとかow.lyとか。を入力します。これはserviceList-domain.txtというファイルにまとめてあります。のでリダイレクトで標準入力から渡してあげてください。    
それを検索キーワードにして　Google Custom Searchで、Twitterを対象に検索してきます。一つのキーワードにつき、デフォルトでは1ページ分(10件の結果が載ってる)しか検索結果はもらっていません。  
検索結果を1件ずつ訪れ、そのサイトの中に対象のドメイン名(与えられたドメイン名リスト全てが対象)を含むURLがないか探してきます。  
25個の検索キーワードでTwitterを対象にすると4分30秒で重複を除いて240個の短縮URLが見つかりました。  



