
import sys
values = [int(e) for e in input("Please insert value:").split()]

max = -sys.maxsize-1 
min = sys.maxsize
total = 0
for value in values:
    if value > max :
        max = value
    if value < min:
        min = value
    total = total + value

total = total - max - min
print(total, max, min)