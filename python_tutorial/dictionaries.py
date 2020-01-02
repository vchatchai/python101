tel = {'jack': 4098, 'sape': 4139}
print('dictionary:', tel)


tel['guido'] = 4127
print("guido = 4127 :", tel)

print('jack', tel['jack'])

del tel['sape']

print('del sape: ', tel)

tel['irv'] = 4127

print('irv = 4127', tel)

print('list(tel)', list(tel))


print('guido in tel', 'guido' in tel)

print('jack not in tel', 'jack' not in tel)

d = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print('dict', d)

d = {x : x ** 2  for x in (2, 4, 6)}
print("power ", d)

d = dict(sape=4139, guido=4127, jack=4098)

print('dict(..)', d)


knights = { 'gallahad': 'the pure', 'robin': 'the brave'}

for k , v in knights.items():
    print(k,v)


questions = ['name', 'quest', 'favorite color']
answers = [ 'lancelot', 'the holy grail', 'blue']

for a in questions : 
    print('question:', a)


for q, a in zip(questions, answers) :
    print('What is your {0}? It is {1}'.format(q,a))