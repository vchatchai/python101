
import math
r1  = [float(e) for e in input("Please insert value:").split()]
r2  = [float(e) for e in input("Please insert value:").split()]

print(r1)
print(r2)
if r1 == r2: 
    print('touch')
elif abs(r1[0]) - abs(r2[0]) < abs(r1[2]) + abs(r2[2]) or ab(r1[1]) - ab(r2[1]) < ab(r1[2]) + ab(r2[2]):
    print('overlap')
else:
    print('free')
    