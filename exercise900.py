import numpy as np


array = np.array([1, 0, 2, 3, -1])
print(array)
multidimensionarray = np.array([[2, 3], [4, 1], [7, 5]])
print(multidimensionarray)
zero = np.zeros((3, 4))
print(zero)
ones = np.ones((3, 3), int)
print(ones)
identity = np.identity(4, int)
print(identity)
zeroeslike = np.zeros_like(array, int)
print(zeroeslike)
oneslike = np.ones_like(array, int)
print(oneslike)
arange = np.arange(4, 10)
print(arange)
arange = np.arange(8.0, 4.0, -1.0)
print(arange)
arange = np.arange(2.3, 2.5, 0.03)
print(arange)

v1 = np.array([1, 2, 3])
v2 = np.array([1, 2, 4])
v3 = v1 + v2
print(v1)
print(v2)
print(v3)
print(1/v2)


A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([9, 8, 7])
C = A + B
print(A.shape)
print(B.shape)
print(C)
print(A*2)

B[1:3] = 99
print(B)

x = np.array([1, 2, 3, 4])
y = np.array([0, -1, 1, 2])
print(x.dot(y))

x = np.array([[1,2],[3,4],[5,6]])
y = np.array([[-2],[3]])
print(x.dot(y))

M = np.array([[1,2,3,4],[5,6,7,8]])
print(np.sum(M))

print(np.sum(M,axis=0))
print(np.sum(M,axis=1))

print(M.T)
print(M > 3)
print(np.sum(M > 3))