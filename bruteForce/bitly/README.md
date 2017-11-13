<!-- # Brute forcing and collecting short URL from goo.gl
Brute forcgin from https://goo.gl/000 to  https://goo.gl/ZZZZZZZZZZ, and collecting valid URL.  
Although it sleeps only 0.05sec every roop, it's too slow.

## Installation
### For using API version
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

# Usage
Fundemental procedure is same as other bruteforcers.

## Remarks
メモ程度に...  
APIなしで直にアクセスすると、時間をある程度開けたとしてもどうやって判断してるのか、そのうち応答してもらえなくなる。  
  
bit.lyはtor使っても使わなくても、応答返さなくなったらブラウザを再起動するとなんとかなる。bit.lyは何入力しても有効なURLで、記号もOKっぽい。無効なURL探す方が大変そうな...    
goo.glより断然、楽。  
あとJavascriptか何か使ってグリグリ動くサイトの中には、画像読み込みをオフにしておくとうまく動かず、socketerr61とかなんとかになることがあり止まってしまう。  
10分で153個、つまり0.255個/秒の探索スピード・有効URL発見スピード。
