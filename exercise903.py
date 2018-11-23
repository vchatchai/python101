import numpy as np


M = np.array([[3,2],[5,6],[7,1]])
print(M)  
xmax = None
xmin = None
ymax = None
ymin = None
for  i,m in enumerate(M) : 
    x1, y1 = m
    for x2, y2 in M[i+1:] : 
        x = abs(x1 - x2)
        y = abs(y1 - y2)
        if xmax ==  None :
            xmax = x
        elif xmax < x :
            xmax = x
        if xmin == None:
            xmin = x 
        elif xmin > x :
            xmin = x
        
        if ymax == None:
            ymax = y
        elif ymax <  y:
            ymax = y
        
        if ymin == None:
            ymin = y
        elif ymin > y:
            ymin = y

print("max:", np.array([xmax, ymax]))

print("min:", np.array([xmin, ymin]))