basket = { 'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print('set', basket)
print('apple in basket:', 'apple' in basket)


print('crabgrass :', 'crabgrass' in basket)
a = set('abracadabra')
b = set('alacazam')

print('a', a)
print('b', b)

print('a - b', a - b)
print('a & b', a & b)
print('a ^ b', a ^ b)


a = { x for x in 'abracadabra' if x not in 'abc'}
print('x in abc ', a)