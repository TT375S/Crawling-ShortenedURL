# Brute forcing and collecting short URL from goo.gl
Brute forcgin from https://goo.gl/000 to  https://goo.gl/ZZZZZZZZZZ, and collecting valid URL.  

## Installation
mainDriver.py needs Python3 and GoogleChrome.  
mainDriver-urllib.py need only Python3.  
mainDriver-curl-header.py need only Pyhton3, too.
<!-- ### For using API version
Need only python3.  

### For non-API version
Need Python3 and selenium, and GoogleChrome.  
`$ brew install python3`  
  
On my Mac, all dependencies are installed by this command.  
`$ pip3 install selenium`  

And get GoogleChrome v.59 or later from [here](https://www.google.com/chrome/browser/desktop/index.html).  

## Usage
### For API version
    $ python3 goo.gl-BFA-API.py
    >Input Google shortener API key
    AIzaSyDIls0IyGAtjdKxUd1Sdd0j-f7kAWEdGRI (<-Your API key)

### For non-API version
`$ pyhton3 goo.gl-BFA-nonAPI-headless.py`
-->

## Usage
    $ <driverFile> <shortURLserviceName> <destinationURLFileName> <shortURLFileName> <startPattern>
  
If you want to bruteforce by using CURL command, and to short URL service "bit.ly", and output destination URL file "dURL-2017-09-01-...txt" and short URL file "sURL-2017-09-01-...txt", and start bruteforce from "aabc", then you should hit ...  
    $ ./mainDriver-curl-header.py bitly dURL sURL aabc
## Remarks
メモ程度に...  
goo.glのAPIの無料版は1秒に1リクエストまで。  
APIなしで直にアクセスすると、時間をある程度開けたとしてもどうやって判断してるのか、そのうち応答してもらえなくなる。  
  
bit.lyはtor使っても使わなくても、応答返さなくなったらブラウザを再起動するとなんとかなる。bit.lyは何入力しても有効なURLで、記号もOKっぽい。無効なURL探す方が大変そうな...    
goo.glはtor必須、応答返さなくなった時のブラウザの再起動も必須。12,090個のURLを346分で試せた。1分あたり34個ということになる。それで得られた有効なURLは3つだけ。  
  
親フォルダbruteforceにあるmaindriver.pyがドライバプログラムで、domainSpecific.pyは短縮URLサービスごとの動作を規定している。  
`$ python3 bitly dURL sURL 0000`  
と打てば、サービスはbitlyで、転送先URLをdURLに、短縮URLをsURLに記録、0000から総当たりを開始、ということになる  
  
bit.lyはtor必要。is.gdもひつよう。tinyurl.comはtor使うと弾かれる？あとow.lyが変なエラーがでる?
