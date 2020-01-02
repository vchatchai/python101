
year = 2016
event = 'Referendum'
output = f'''test fancier {year} {event}'''
print(output)

yes_votes =  42_572_654
no_votes = 43_132_495

percentage= yes_votes / no_votes

output2 = '{:-9} YES votes {:2.2%}'.format(yes_votes, percentage)
print(output2, yes_votes)


s = 'Hello, world.'
print(str(s), repr(s))
print(str(1/7), repr(1/7))

x = 10 * 3.25
y = 200 * 200

s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
print(s)


hello = 'hello, world\n'
hellos = repr(hello)
print(hellos)
triplesquote = '''

Test

Ja
'''

print(repr(triplesquote))


