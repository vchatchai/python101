# import sound.formats
from sound.formats import wareread


if __name__ ==  "__main__" :
    print("main")
    print(wareread.waveRead())


listOne = [10, 20, 23, 11, 17]
listTwo = [13, 43, 24, 36, 12]

# setOne = set(listOne)
# setTow = set(listTwo)
 


# result = setOne & setTow
result = listOne[:] + listTwo[:]
print(result)