import math

a = int(input("Please  insert value:"))

x = int(a**(1/3))
x3 = x**3
print(x3, a)
if a != x3:
    print("Not Found")
else :
    print(a)
