import sys
import json
import re
inputFileName = "logCommit.txt"

if len(sys.argv) >=2:
    inputFileName = sys.argv[1]

f = open(inputFileName)
jsonData = json.load(sys.stdin)
f.close()

items = jsonData["items"]
print("items:" + str(len(items)) )
for item in items:
    commit = item["commit"]
    commitMessage = commit["message"]
    urls = re.findall('(?:https?:\/\/|)[^\s ]+\/[0-9a-zA-Z]*' , commitMessage)
    for url in urls:
        print(url)
