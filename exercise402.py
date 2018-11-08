import sys

print(sys.version)

# values = input("Please insert value: ")

values = "pythonnnaa"
result =  []
count = 0 
for value in values : 
    # if len(result) > 0  and  result[len(result)-1] != value and  result[len(result)-2] != result[len(result)-1] :     
    #     result.append(result[len(result)-1])
    
    if len(result) > 0  and  result[len(result)-1] == value:
        count = count + 1
    elif len(result) > 0 and count == 0:
        count = 0
        result.append(result[len(result)-1])
    else:
        count = 0
    result.append(value)
    


for v in result :
    print(v, end="")


print()

# 'ppyytthhoonnnaa'