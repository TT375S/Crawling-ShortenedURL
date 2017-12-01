# Usage
Need Python3.  

Install 2 packages.
`$ pip3 install requests requests_oauthlib` 

# Remarks
ツイッターのpublic streamから情報を取ってくるやつ。
キーワードとして"twitter"を指定するとなぜかたくさん取れる。下手に"t.co"とか指定してもなぜかあまりひっかからない。  
ユーザーが貼った有効なURLは全てt.coに変換されてしまう。このAPIで取ってきたやつは、全て変換されたあとのt.coになってるっぽい。(アプリだと表示上は元のURLで、リンク先だけt.coになるのだが、元のURLの取得はできない？)   
  
なお、再接続の処理ができてないかもしれない。
また、リザルトが空のままの時があるが、そのときは何秒か待った方がいい
