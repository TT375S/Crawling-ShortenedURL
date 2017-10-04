import re
import sys

print (re.findall('tinyurl.com'+  '(?:</em>|)' + '/[0^9a-zA-Z]*', input() ))

