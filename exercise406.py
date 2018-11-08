

values = input("Please fill value:")

result = []

for value in values : 

    if str(value).isdigit() :
        dec = int(value)
        if dec % 2 != 0 :
            result.append(dec)

print(result)
print(len(result))