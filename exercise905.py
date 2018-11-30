import numpy as np

k = 10

C = np.zeros((k, k))
C[1::2, 0::2] = 1
C[0::2, 1::2] = 1
print(C)
