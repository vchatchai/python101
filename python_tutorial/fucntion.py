
def fib(n):
    a, b = 0, 1
    result = []
    while a < n :
        print(a, end = ' ')
        result.append(a)
        a, b = b, a + b
        
    print()
    return result

result = fib(2000)
print(result)