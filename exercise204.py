
values = [int(e) for e  in input("Please insert value:").split()]
print(values)
previousValue  = values[0]
for value in values :
    if value < previousValue : 
        previousValue = value
        print("False")
        exit(0)
           


print("True")
