"""
Pseudo Code:
Inventory Application:

A way to store inventory
A way to store users
Edit users and inventory
A way to link the two

We will need 2 classes:
class 1 = Inventory
class 2 = User

first_name
firstName

"""

class User:
    def __init__(self, firstName, lastName, username, age, email):
        self.firstName = firstName
        self.lastName = lastName
        self.username = username
        self.age = age
        self.email = email
        self.inventoryList = []
        self.location = None

    def printUser(self):
        print(f"{self.firstName} {self.lastName}")

    def addLocation(self, location):
        self.location = location
        print(f"{self.firstName} is located at {self.location}")
        return self

    def printMore(self):
        print(f"{self.firstName} {self.lastName} is located at {self.location}")

# This function allows the 2 classes to talk to each other by appending the items
    def addItems(self, item):
        self.inventoryList.append(item)
        return self

    def printInventory(self):
        theList = []
        for i in self.inventoryList:
            theList.append(i.itemName)
        print(f" {self.firstName} has the following items: {theList}")

class Inventory:
    def __init__(self, itemName):
        self.itemName = itemName
        self.itemLocation = None
    
    def addLocation(self, itemLocation):
        self.itemLocation = itemLocation
        return self


# Create new Users
eion = User("Eion", "PenGryphon", "epg", 30, "eion@email.com")
paige = User("Paige", "Milosevic", "paperPaiges", 25, "paige@email.com")
melissa = User("Melissa", "Longenberger", "honeybee", 43, "melissa@email.com")


# create Items
laptop = Inventory("Laptop")
clock = Inventory("clock")

# adding items to the User inventoryList attribute
eion.addItems(laptop)
paige.addItems(laptop).addItems(clock)

# printing inventory
paige.printInventory()
eion.printInventory()

# Add location
eion.addLocation("Melissa's Python Class")
paige.addLocation("USA").printUser()
melissa.addLocation("Berwick, PA").printUser()


# Print User
eion.printUser()
eion.printMore()