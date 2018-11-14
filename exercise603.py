numberMap = {}
maxValueKey= None
with open('data.txt', 'r') as data :
    for line in data :
        number = int(line)
        value = None
        if number in numberMap :
            value = numberMap[number] +  1
        else :
            value = 1
        numberMap[number] = value


        if maxValueKey == None or value > numberMap[maxValueKey]:
            maxValueKey = number

print('max number', maxValueKey)
print(numberMap)