import sys
import re

lengths = [0 for i in range(100)]

domain ="" 

if len(sys.argv) >= 2:
    domain = sys.argv[1]
else:
    print("specify domain!", file=sys.stderr)
    exit()
try:
    while(1):
        currentText = input()
        urlPath = re.sub("(?:https?:\/\/|)"+domain +"\/", "", currentText)
        length = len(urlPath)
        #print(urlPath)
        if length == 1:
            print(currentText, file=sys.stderr)
        #print("len:" + str(length))
        lengths[length] += 1
except EOFError:
    for i, v in enumerate(lengths):
        print(str(i) + ", " + str(v))    

    
