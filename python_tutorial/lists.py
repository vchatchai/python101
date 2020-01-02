squares = [1,4,9,16,25]
print(squares)
print(squares[-1])
print(squares[ 0: ])

quares = squares + [36,49,64,81,100]
print(quares)

quares = quares[:] * 3   
print(quares)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letters[2:5] = ['C', 'D', "E"]
print(letters)
print(len(letters))

words = ['h', 'i', 'j']

total = [words, letters]
print(total)