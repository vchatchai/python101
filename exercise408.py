

values = input("Please file binary value:")

result = 0
count = 1
for value in values :
    result = result + int(value) * (2 ** (len(values) - count) ) 
    x =  ( (len(values) - count) ) 
    count = count + 1 

print(result)