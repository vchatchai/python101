# integer  = int(input("Please fill number:"))
integer = 1231123

result = tuple()
for i in str(integer):
    result = result + (int(i),)

print(result)