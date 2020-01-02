import sys
print(sys.__name__)

print(sys.path)

import fibo

for value in dir(fibo) :
    print(value)

print(fibo.__builtins__) 
print("sys")
for value in dir(sys) :
    print(value)


import builtins 

for value in dir(builtins):
    print(value)