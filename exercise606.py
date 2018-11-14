

lineLength = {}
with  open('data606.txt', 'r') as file :
    for line in file:
        line = line.strip()
        lines = lineLength.get(len(line))
        print(not lines)
        if not lines :
            lines = []
            lineLength[len(line)] = lines
        lines.append(line)
        lines.sort()

print(lineLength)

keys = list(lineLength.keys())
keys.sort()

for value in  keys:
    print("length {} : {}".format(value, lineLength[value]))