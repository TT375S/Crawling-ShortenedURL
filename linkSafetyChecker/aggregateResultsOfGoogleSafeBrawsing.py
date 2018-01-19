import sys, json;

data = json.load(sys.stdin)

urlDic = {}

threatTypeDic = {}
platformTypeDic = {}

for result in data["matches"]:
    url = result["threat"]["url"]
    threatType = result["threatType"]
    platformType = result["platformType"]

    urlDic.setdefault(url, []) 
    urlDic[url].append( (threatType, platformType) )
    
    threatTypeDic.setdefault( threatType, {})
    threatTypeDic[threatType].setdefault(platformType, 0)
    threatTypeDic[threatType][platformType] += 1

    
    platformTypeDic.setdefault( platformType, {})
    platformTypeDic[platformType].setdefault(threatType, 0)
    platformTypeDic[platformType][threatType] += 1
#print(urlDic)
print(threatTypeDic)
print(platformTypeDic)
