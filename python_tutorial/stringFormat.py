print('We are the {} who say "{}!"'.format("knights", 'Ni'))
print('{1} and {0}'.format('spam', 'eggs'))
print('This {food} is {adjective}.'. format( food = 'spam', adjective='absolutely horrible'))
print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred', other='Georg'))

table = {'Sjoerd': 4127, 'Jack' : 4098, 'Dcab': 8637678 }

print('Jack: {0[Jack]: d}; Sjoerd: {0[Sjoerd]:d};'
    'Dcab: {0[Dcab]:d}'.format(table))
x = 123
x = '{}'.format(x)
x.zfill(8)
print(x)