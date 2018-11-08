values = input("please fill value: ")

previous = []
result = []



def isAEIOU(value):
    # value = str(value)
    if value.upper() == 'A':
        return True
    elif value.upper() == 'E':
        return True
    elif value.upper() == 'I':
        return True
    elif value.upper() == 'O':
        return True
    elif value.upper() == 'U':
        return True
    return False

for value in values :
    if isAEIOU(value) :
        previous.append(value)
        if len(previous) > 1:
            result.append(''.join(previous))
    else :
        previous.clear()
    
    
print(len(result))
print(result)