# Brute forcing and collecting short URL from goo.gl
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

## Remarks
メモ程度に...  
goo.glのAPIの無料版は1秒に1リクエストまで。  
APIなしで直にアクセスすると、時間をある程度開けたとしてもどうやって判断してるのか、そのうち応答してもらえなくなる。  

bit.lyも同じ。torを使ってIPアドレス変えつつアクセスしてもダメ。goo.glはtorで試してないけど、GoogleはTorとかそういうの厳しそうなので多分同じ。  
