import math

x = [int(e) for e in input().split()]

print(x)

if x[0] > x[1]:
    x[1],x[0] = x[0],x[1]

if x[0] > x[2]:
    x[0], x[2] = x[2], x[0]

if x[1] > x[2]:
    x[2], x[1] = x[1], x[2]


print(x[1])