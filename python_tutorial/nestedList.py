matrix = [ 
    [1, 2, 3, 4], 
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

print("matrix:", matrix)

result = [[row[i] for row in matrix] for i in range(4)]
print("[3 x 4] => ", result)

transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])

print("transposed => ",transposed)

transposed.clear() 
for i in range(4):
    transposed_row  = []
    for row in matrix : 
        transposed_row.append(row[i])
    transposed.append(transposed_row)

 



print("transposed2  => ",transposed)


result = list(zip(*matrix))
print("matrix => ",result)


del matrix[:1]

print("del matrix:", matrix)