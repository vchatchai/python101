for element in [1,2,3]:
    print(element)
for element in (1,2,3):
    print(element)
for key in {'one': 1, 'two':2}:
    print(key)
for char in "123" :
    print(char)

s = 'abc'
it = iter(s)

print(next(it))
print(next(it))
print(next(it))


class Reverse:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

rev = Reverse('spam')
iter(rev)
for char in rev :
    print(char)