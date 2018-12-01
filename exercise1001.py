class Nisit:
    def __init__(self, name, year, faculty):
        self.name = name
        self.year = year
        self.faculty = faculty

    def __str__(self):
        return '{} (year {}) Enginering'

    def __lt__(self, rhs):
        if self.faculty != rhs.faculty:
            return self.faculty > rhs.faculty
        elif self.year != rhs.year:
            return self.year > rhs.year
        else:
            return self.name > rhs.name


a = Nisit('Krit', 4, 'Engineering')
b = Nisit('Krit', 3, 'Engineering')

print(Nisit.__lt__(a,b))