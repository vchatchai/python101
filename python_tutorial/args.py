import sys


for value in sys.argv : 
    print(value)


def this_fail():
    return 1/0

try:  
    this_fail()

except Exception as err: 
    print("Handlering run-time error", err)

def bool_return() :
    try:
        return True 
    finally:
        return False

print(bool_return())