import sys

lengths = [0 for i in range(100)]

offset = 0
if len(sys.argv) >= 2:
    offset = len(sys.argv[1])
else:
    print("default offset is 0", file=sys.stderr)

try:
    while(1):
        length = len(input()) - offset
        #print("len:" + str(length))
        lengths[length] += 1
except EOFError:
    for i, v in enumerate(lengths):
        print(str(i) + ", " + str(v))    

    
