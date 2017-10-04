# coding: UTF-8
import urllib2

url = "https://twitter.com/search?q=tinyurl&src=typd"
res = urllib2.urlopen(url)
data = res.read()
print data
