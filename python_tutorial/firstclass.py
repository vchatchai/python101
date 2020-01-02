class MyClass : 
    """A Simple  example class """ 
    i = 12345 

    def f(self):
        return f'Hello world {self.i}'



myClass = MyClass()
print(myClass.__doc__)
print(myClass.f())