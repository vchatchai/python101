
values =  str(input('Please insert value: '))
print(values)
result = 0
length = len((values))
for  x in range( length  ):
    print(str(x) + " " + values[x])
    result += ( 10 - x ) * int(values[x])


print(result)

print(values + str(11-(result%11)))