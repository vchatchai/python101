k = 1
for i in range(1000):
    k *= (365 - i)/365
    print(k)
    if (1 -k) >= 0.5 :
        print(i)
        break