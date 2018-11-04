
x,y = [float(e) for e in input("Please insert value:").split()]


if ( x >= 0) & ( y >= 0):
    print("+,+")
elif( x >= 0) &( y < 0): 
    print("+,-")
elif (x < 0) &( y < 0):
    print("-,-")
else :
    print("-, +")