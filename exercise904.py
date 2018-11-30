import numpy as np

X = np.array([[3,4],[5,12],[24,7]])
print(X)
X = X ** 2
print(X)
X =  np.sum(X, axis=1)
print(X)
X = np.sqrt(X)
print(X)
