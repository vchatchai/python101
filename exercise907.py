import numpy as np

catogory = np.array([50,30,40,20])

data = np.array([
[20,50,10,15,20],
[30,40,20,65,35],
[75,30,42,70,45],
[40,25,35,22,55]])

print(catogory)
print(data)
print(catogory.dot(data))
print(data.T.dot(catogory))
