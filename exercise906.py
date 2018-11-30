import numpy as np

k = 10

C = np.zeros((k, k))
C[0::2, 0::2] = 1
C[1::2, 1::2] = 1

for idx,  c in enumerate(C)  :
    r = np.multiply(c, (idx +1))
    C[idx] = r

print(C)
