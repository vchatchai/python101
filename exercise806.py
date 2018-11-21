def a(n): 
    even = n % 2
    if n == 1 :
        return 1
    elif n == 2:
        return 2
    else :
        if even == 0 and n > 0:
            return a(n/2) + (a(n/2)%10)
        elif even == 1 and n > 0:
            return a(int((n-1)/2)-1)*((n-1)/2)
print(a(5))