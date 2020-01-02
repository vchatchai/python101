class MyClass : 
    """A simple  example class"""
    i = 12345
    def __init__(self) : 
        self.data = []

    def f(self) :
        return 'hello world'

x = MyClass()

print(x.f())


class Complex:
    def __init__(self, realpart, imagpart) : 
        self.r = realpart
        self.i = imagpart


c = Complex(3.0, -4.5)

print((c.r, c.i))

x.counter = 1
print(x.counter)

while x.counter < 10:
    print(x)
    x.counter = x.counter * 2

print(x.counter)
del x.counter


xf = x.f
print(xf())
print(MyClass.f(x))