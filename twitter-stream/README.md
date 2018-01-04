#Twitter-Stream API
## Usage
### Collecting URL
Need Python3.  

Install 2 packages.
`$ pip3 install requests requests_oauthlib` 
  
And It needs Twitter account information. For details, read scripts.  
    #consumer Vey, consumer secret, access token, access secret.
    ckey  = ""
    csecret = ""
    atoken = ""
    asecret = ""
 
Execute. And input keyword "http".   
    $ ./streamingShortUrl-tweepy.py 
    http
  
If you want to collect only "bit.ly", execute "streamingShortUrl-tweepy-forBitly.py".

### shor URL lengths
`$ python3 ./urlLengthCount.py < targetFile.txt`

## Remarks
ツイッターのpublic streamから情報を取ってくるやつ。
キーワードとして"twitter"を指定するとなぜかたくさん取れる。下手に"t.co"とか指定してもなぜかあまりひっかからない。  
ユーザーが貼った有効なURLは全てt.coに変換されてしまう。このAPIで取ってきたやつは、全て変換されたあとのt.coになってるっぽい。もちろん元のURLも取得できる  
    
切断された場合、無限ループになっているので再接続する。  
これらは、すべての処理を一つの関数にして、try-catchで全部の例外を補足することによって解決した。  
例外を投げそうな部分でtry-catchしただけだと、変なタイミングで例外が発生した時にcatchできない？pythonの仕組みよくわかってない
  
どうやら、許容量以上のストリーミングが起こると切断される模様。  
また、リザルトが空のままの時があるが、そのときは何秒か待った方がいい  
  
