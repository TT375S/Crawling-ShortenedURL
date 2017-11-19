import requests
from requests_oauthlib import OAuth1
import json

#complete below 4 parameters
api_key = ""
api_secret = ""
access_token = ""
access_secret = ""

url = "https://stream.twitter.com/1.1/statuses/filter.json"

auth = OAuth1(api_key, api_secret, access_token, access_secret)

#r = requests.post(url, auth=auth, stream=True, data={"follow":"nasa9084","track":"emacs"})
r = requests.post(url, auth=auth, stream=True, data={"track":"twitter"})

for line in r.iter_lines():
  print(line)
  try:
      jsonData = json.loads(line)
      print("BUGBUG")
      print(jsonData["text"])

      print("BUGBUG2")
  except:
      print("ERR")
