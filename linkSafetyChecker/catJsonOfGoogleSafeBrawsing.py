#coding:utf-8
import sys;

for fileInd in range(1, len(sys.argv)):
    with open(sys.argv[fileInd],'r') as f:
        
        #print(sys.argv[fileInd])
        lineNum = 0
        lines = f.readlines()
        num_lines = len(lines)
        
        #print(num_lines)
        #print(f.readlines()[1])
        
        startLine = 0
        endLine = num_lines-1 -2
        if fileInd >= 2:
            startLine = 2
             
        for row in lines[startLine : endLine]:
            print(row.replace("\n", ""))

print("] }")
