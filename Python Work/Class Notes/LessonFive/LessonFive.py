"""
    7/6/15
    Object Oriented Programming
"""

class Animal(object):
    def __init__ (self):
        self.numLegs = 4
        self.color = "brown"

    def eat(self):
        print("Nom nom. I ate the world.")
"""
anAnimal = Animal()
print(anAnimal)
print(Animal)
anAnimal.eat()
"""

class Cat(Animal):
    pass

"""
aCat = Cat()
print(aCat)
aCat.eat()
print(aCat.color)
"""

class Dog(Animal):
    def eat(self):
        print("Nooooooom Noooooooom! BACON!!!")

    # def eat(self, food):
    #     print("Eating more... I want more {0}"
    #           .format(food))
'''
aDog = Dog()
aDog.eat()
'''
