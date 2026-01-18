# Inheritance: it allows class to inherit attributes and methods from another class
# Helps code reusability and extendibility
# For instance - class Child(Parent)



class Vehicle:

    def __init__(self, types, speciality):
        self.types = types
        self.speciality= speciality

    def start(self):
        print('The vehicle is starting. ')
    def brake(self):
        print('The vehicle has braked. ')


class Ferrari(Vehicle):
    def speed(self):
        print('The maximum speed is 150mph. ')

class BMW(Vehicle):
    def fuel(self):
        print('It can last up to 1 week for full tank.')

class Honda(Vehicle):
    def safe(self):
        print('This vehicles has high safety. ')


car1=Ferrari('Electric', "High speed")
car2= BMW('Manual', 'High fuel')
car3= Honda('Self-driving','Safe')

car1.speed()
car2.fuel()