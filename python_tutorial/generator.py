def reverse(data):
    for index in range(len(data)-1, -1, -1) :
        yield data[index]


for char  in reverse('golf') :
    print(char)


#generator expression
print(sum(i*i for i in range(10)))


xvec = [10,20,30]
yvec = [7, 5, 3]
result = sum(x*y for x,y in zip(xvec, yvec))
print(result )

data = 'golf'
result = list(data[i] for i in range(len(data)-1, -1, -1))
print(result)