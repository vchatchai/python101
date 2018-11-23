import numpy as np


M = np.array([[1,2,3,4,5,6],[7,8,9,10,11,12]])
k = 3
print(M)
M[M%k == 0] = 0
print(M)
