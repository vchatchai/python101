
values = []
while True :
    value = input("Fill value:")
    if str(value).isdigit() :
        values.append(int(value))
    else:
        break

print(values)
values.sort()
print(values, sep=',')