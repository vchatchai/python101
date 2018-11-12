
v1 = [float(e) for e in input('Input fill value:').split()]

v2 = [float(e) for e in input('Input fill value:').split()]


print(v1)
print(v2)

if len(v1) != len(v2) :
    print("length v1 and v2 is not equal")
else:
    result = [v1[i] * v2[i] for i in range(len(v1))]
    print(result)
        