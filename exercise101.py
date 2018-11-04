import math
import random



h,m,s =  [ int(e) for e in  input("insert value:")  ]

s += m * 60
s += h * 60 * 60

print(h,m,s)

print(s)