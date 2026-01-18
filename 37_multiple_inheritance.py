# multiple inheritance: inherits from more than one parent class

# multilevel inheritance: inherits from parents and that parent class inheritance from another parent class


class Animal():
    def __init__(self, name):
        self.name= name
    def eat(self):
        print(f'{self.name} is eating')

    def sleep(self):
        print(f'{self.name} is sleeping')

    

class Prey(Animal):
    def flee(self):
        print(f'{self.name} is fleeing')
    
class Predator(Animal):
    def hunt(self):
        print(f'{self.name} is hunting. ')


class Rabbit(Prey):
    pass

class Leopard(Predator):
    pass

class fish(Prey, Predator):
    pass


rabbit= Rabbit("Helium")
leopard= Leopard("Billy")
Fish = fish('Sweety')

rabbit.sleep()
rabbit.flee()
Fish.hunt()