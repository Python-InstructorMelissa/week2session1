
"""
Our Pseudo code
Parks:
Employees
shops
park type
location
attractions

class 1 = the parks themselves
class 2 = the workers
"""

# Our 1st Class = Our workers Line 17 is all the parameters that are required when creating a new instance of an employee, lines 18-22 define what those parameters are.
class Employee:
    def __init__(self, firstName, lastName, employeeId, email, hireDate):
        self.firstName = firstName
        self.lastName = lastName
        self.employeeId = employeeId
        self.email = email
        self.hireDate = hireDate

# Here we are creating simple functions to just print a line with the instance that we call
    def welcomeEmployee(self):
        print(f"Welcome to our company {self.firstName} {self.lastName}!")

    def employeeInfo(self):
        print(f"{self.firstName} was hired on {self.hireDate}, with an email address of {self.email}")


# Our 2nd Class = Our parks.  Line 34 is where we are declairing the name of our organization.  Line 35 is where have all the required parameters when creating new instances of a park.  Lines 38, 39, & 44-46 are all parameters that are not required of all instances but may be used for any of them.
class Park:
    ourOrganization = "Unpaid Workers Association"
    def __init__(self, parkName, location, parkType, tickets, hours, parking):
        self.parkName = parkName
        self.location = location
        self.shops = []
        self.attractions = []
        self.parkType = parkType
        self.tickets = tickets
        self.hours = hours
        self.parking = ''
        self.animals = []
        self.plant = []
        self.employees = []

# Here are our simple print statements to provide some information of our newly created instances

    def welcome(self):
        print(f"Welcome to {self.parkName}, we are a(n) {self.parkType} located in {self.location}. The cost to enter is ${self.tickets}.  At this time our hours of operation are {self.hours} and we have the following parking accommodations, {self.parking}")

    def listShops(self):
        print(f"Here are the different shops that we have on site {self.shops}")
        
    def listEmployees(self):
        print(f"Here is a list of the staff at {self.parkName}: {self.employees[0].firstName}") # Because we did NOT use a for loop in this function we are only able to print 1 employee's name and only the one at the index provided in this function.  A for loop would work best so that it can print all employee's by name.

    # Better way to do the above function
    def listAllEmployed(self):
        employedNames = []
        for e in self.employees:
            employedNames.append(e.firstName)
        print(f"Here is a list of those employed at {self.parkName}: {employedNames}")

    def plantTypeCount(self):
        count = len(self.plant)
        print(f"At {self.parkName} we have {count} different types of Plant(s)")

#  Here is where we are creating a function to add those optional requirements
    def addShop(self, shopType):
        self.shops.append(shopType)


    def addEmployee(self, worker):
        self.employees.append(worker)

    def addPlant(self, plantType):
        self.plant.append(plantType)



# Creating Employee instances:
alice = Employee("Alice", "Inchains", 8675309, "alice@email.com", "April 20th, 2020")
bob = Employee("Bob", "Cat", 2, "bob@email.com", "April 20th, 2020")
jane = Employee("Jane", "Doe", 22, 'jane@email.com', "October 1, 2020")
john = Employee("John", "Smith", 33, 'john@email.com', "October 1, 2020")

# Creating Park instances
park01 = Park("Lego Land", "San Diego, CA", "Amusement Park", 300, "8am - 10pm Tuesdays, Thursdays, & Sundays", "1st come 1st serve")
park02 = Park("Zootopia", "Icelandia", "Zoo", 50, "10am - 10pm 7 Days a week", "7 dedicated locations for parking")
park03 = Park("HoneyBee Botanicals", "Berwick, PA", "Botanical Garden", 10, "10am-9pm Monday-Saturday", "50 Dedicated parking spots")

# Printing statements for employees

alice.welcomeEmployee()
bob.welcomeEmployee()
alice.employeeInfo()
bob.employeeInfo()

# Printing statements for parks
park01.welcome()
park02.welcome()
park03.welcome()

# Using the functions inside the park to add shops

park01.addShop("Ice Cream Parlor")
park01.addShop("Food Shoppe")
park01.addShop("Lego Land Store")

# Printing the shops we just added
park01.listShops()

# adding and then printing the employee at the park
park01.addEmployee(alice)
park01.listEmployees()
park01.addEmployee(john)

park01.listAllEmployed()

park03.addPlant("Lilies")
park03.addPlant("Roses")
park03.addPlant("Tulips")

park03.plantTypeCount()

