from os import listdir
from os import path

p = input("Please fill path:")

if path.exists(p) :
    list = listdir(p)
    for f in list  :
        print(f)

