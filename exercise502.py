

fileLines = open('exercise101.py','r')
lines = fileLines.readlines()

for line in range(len(lines)-1,0, -1):
    lineStr = lines[line] 
    if len(lineStr.strip()) > 0 :
        print(lineStr, end="")