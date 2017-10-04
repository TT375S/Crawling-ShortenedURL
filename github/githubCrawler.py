# -*- coding: utf-8 -*-

import urllib.parse
import urllib.request

#IMPORTANT: urllib.request encodes the target URL with ASCII. 
# If the URL contains non-ascii character, it should be encoded UTF-8 by using urllib.parse.
url = "http://github.com/search?utf8=✓&q=tinyurl.com&type="

with urllib.request.urlopen(urllib.parse.quote_plus(url, "/:?=&")) as response:
   html = response.read().decode('utf-8')
   print(html)
