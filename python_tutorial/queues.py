from collections import deque
valuesList = ["Eric","John", "Michael"]
queue = deque(valuesList)
print(queue)
queue.append("Terry")
queue.append("Graham")
print(queue)

print(queue.popleft())
print(queue.popleft())
print(queue)