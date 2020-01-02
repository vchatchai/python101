string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
non_null = string1 or string2 or string3

print(non_null)


print((1, 2, 3) == (1, 2, 3))
print((1, 2, 3) == (1.0, 2.0, 3.0 ))
print((1, 2, 3) == (1, 2, 4))
print((1, 2, 3) == (1, 2, 3,5))

print((1, 2, 3) == [1, 2, 3])

print([1, 2, 3] == [1, 2, 3])


print('ABC'< 'C' < 'Pascal' < 'Python')