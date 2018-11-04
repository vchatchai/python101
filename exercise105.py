import math

x1, y1, x2, y2 =  [ float(e) for e in input("Please insert value: ").split()  ]
print(x1, y1, x2, y2)
#print(i.split())
#x1, y1, x2, y2  =  [ e for e in input("Please insert value: ")]

y = (y1 - y2)
x = (x1 - x2)

result = math.sqrt(y**2 + x**2)

print(result)
