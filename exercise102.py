import math

x = float(input("Please fill real number:"))

print('x**x', x**2)

y = 2 - x + ((3/7)*(x**2) )- (5/11)*(x**3) + math.log10(x)

print("result formular:", y)