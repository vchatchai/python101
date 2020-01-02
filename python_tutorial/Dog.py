class Dog:
    kind = 'canine'
    tricks = [] #mistaken use
    
    def __init__(self, name):
        self.name = name
        self.tricksInstance = []
    def add_trick(self, trick): 
        self.tricks.append(trick)

    def add_trick_instance(self, trick):
        self.tricksInstance.append(trick)

d = Dog('Fido')
e = Dog('Buddy')
print(d.kind, d.name)
print(e.kind, e.name)

d.add_trick('roll over')
e.add_trick('play dead')

print(d.tricks)

d.add_trick_instance('roll over')
e.add_trick_instance('play dead')


print(d.tricksInstance)
print(e.tricksInstance)
