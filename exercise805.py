def a(n): 
    if n == 0:
        return 1
    elif n == 1:
        return -2
    else :
        return a(n-2) *n

print(a(5))