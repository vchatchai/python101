t = 12345, 54321, 'hello!'
print('tuples',t)

u = t, (1,2,3,5,6)

print('nest', u)

v = ([1, 2, 3], [3, 2, 1])
print('tuples list', v)
v[0][0] = 10

print('tuples list change', v)


x, y,z = t

print(x,y,z)