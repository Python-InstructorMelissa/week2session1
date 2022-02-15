"""
Our Pseudo code
Class name = Pets
Owner class
Food class
Tricks class
Attributes => name, gender, breed, age
Methods => sleep, eat

"""
class Pets: # the name of the class must always be capitalized
    def __init__(self, name, gender, breed, age): # constructor funcion tells us or defines the attributes that each instance of the class can have
        self.name = name
        self.gender = gender
        self.breed = breed
        self.age = age
        self.food = None
    
    def printPet(self):
        print(f'{self.name} is a {self.gender} {self.breed} dog that is {self.age} old.')

    def eat(self, food):
        self.food = food.name
        print(f'{self.name} likes to eat {self.food}')

class Food:
    def __init__(self, name):
        self.name = name

    def printFood(self):
        print(f'Food item: {self.name}')

    
class Owner:
    def __init__(self, name):
        self.name = name
        self.pets = []

    def printOwner(self):
        print(f'{self.name} is a pet owner')

    def printPetsOwned(self):
        thePets = []
        for p in self.pets:
            thePets.append(p.name)
        print(f'{self.name} owns the following pet or pets {thePets}')
    
    def addPet(self, pet):
        self.pets.append(pet)
        self.printPetsOwned()
        return self

# Creating instances of our Pet class
copper = Pets('Copper', 'Male', 'Beagle', '1 year')
bear = Pets('Bear', 'Male', 'Shepherd Mix', '7 years')
roxy = Pets('Roxy Mae', 'Female', 'Red nose Pit Shepherd mix', '1.5 years')
lucy = Pets('Lucy', 'Female', 'Chawinnie', '5 years')

# Creating instances of Owners
melissa = Owner('Melissa')

# Creating an instance of Food
beneful = Food('Beneful')

# Using our methods
copper.printPet()
bear.printPet()

melissa.addPet(copper)
melissa.addPet(bear)

roxy.eat(beneful)