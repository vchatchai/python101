# integer  = int(input("Please fill number:"))
integer = 12

result = tuple()
for i in range(0,integer,2 ):
    result = result + (i,)

print(result)