fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print('count', fruits.count('apple'))
print('index', fruits.index('banana'))
print('index start4', fruits.index('banana',4))
fruits.reverse()
print('reverse',fruits )
fruits.append('grape')
print('append', fruits)
fruits.sort()
print('sort', fruits)
print('pop', fruits.pop())
fruits.clear()
print("clear", fruits)