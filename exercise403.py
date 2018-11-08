import sys

print(sys.version)
value = str(input("Please insert text: "))
palindrome = value[-1::-1]
if palindrome == value :
    print("Y")
else :
    print("N")