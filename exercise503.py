

fileLines = open('exercise101.py','r')

lines = fileLines.readlines()

writer = open('reverse.txt', 'w')

for lineNumber in range(len(lines)- 1, 0, -1) :
    line = lines[lineNumber]
    if len(line.strip())> 0 :
        writer.write(line)
writer.close()
fileLines.close()
