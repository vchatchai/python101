import math 
print(f'The value of pi is approximatly {math.pi:.3f}')
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items() :
    print(f'{name:10} ==> {phone:10d}')

animals = 'eels'
print(f'My hovercraft is full of {animals}')
print(f'My hovercraft is full of {animals!r}')

test = 'ภาษาไทย'

print(f'{test!a}')