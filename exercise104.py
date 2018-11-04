import math


v1,v2,v3 = [float(e)  for e in input("Please insert value: ")]
u1,u2,u3 = [float(e) for e in input("Please insert value: ")]
v = (v1,v2,v3)
u = (u1,u2,u3)
print(v)
print(u)
result = sum([i*j for (i, j) in zip(v,u)])
print(result)