# Class: attributes (property), method
# Object: attributes (property), method

# attribute: class and object

class Car:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Car(name='{self.name}')"


class Person:
    persons = []

    def __init__(self, name, age):
        self.name = name
        self.age  = age
        self.cars = []

        Person.persons.append(self)

    def add_car(self, car):
        self.cars.append(car)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"

c01 = Car('BMW')
c02 = Car('NEXIA')
c03 = Car('Lacetti')

p01 = Person('Ali', 17)
p01.add_car(c01)
p01.add_car(c03)

p02 = Person('Vali', 13)
p02.add_car(c02)

p03 = Person('Sami', 13)
p04 = Person('Gani', 13)
p05 = Person('Bob', 13)

print(p01.cars)
print(c01)

print(p01.persons)
