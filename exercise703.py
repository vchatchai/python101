# values  = input("Please fill number:")
values = "abacdwew"

result = {}
for i in str(values):
    if result.get(i) == None :
        result[i] = 0
    result[i] = result.get(i) + 1

print(result)