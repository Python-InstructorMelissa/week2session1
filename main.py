
"""
Parks:
Employees
shops
park type
location
attractions

class 1 = the parks themselves
class 2 = the workers
"""
class Employee:
    def __init__(self, firstName, lastName, employeeId, email, hireDate):
        self.firstName = firstName
        self.lastName = lastName
        self.employeeId = employeeId
        self.email = email
        self.hireDate = hireDate

    def welcomeEmployee(self):
        print(f"Welcome to our company {self.firstName} {self.lastName}!")

    def employeeInfo(self):
        print(f"{self.firstName} was hired on {self.hireDate}, with an email address of {self.email}")

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

    def welcome(self):
        print(f"Welcome to {self.parkName}, we are a(n) {self.parkType} located in {self.location}. The cost to enter is ${self.tickets}.  At this time our hours of operation are {self.hours} and we have the following parking accommodations, {self.parking}")

    def addShop(self, shopType):
        self.shops.append(shopType)

    def listShops(self):
        print(f"Here are the different shops that we have on site {self.shops}")

    def addEmployee(self, worker):
        self.employees.append(worker)

    def listEmployees(self):
        print(f"Here is a list of the staff at {self.parkName}: {self.employees[0].firstName}") # Because we did NOT use a for loop in this function we are only able to print 1 employee's name and only the one at the index provided in this function.  A for loop would work best so that it can print all employee's by name.


# Creating Employee instances:
alice = Employee("Alice", "Inchains", 8675309, "alice@email.com", "April 20th, 2020")
bob = Employee("Bob", "Cat", 2, "bob@email.com", "April 20th, 2020")

# Creating Park instances
park01 = Park("Lego Land", "San Diego, CA", "Amusement Park", 300, "8am - 10pm Tuesdays, Thursdays, & Sundays", "1st come 1st serve")
park02 = Park("Zootopia", "Icelandia", "Zoo", 50, "10am - 10pm 7 Days a week", "7 dedicated locations for parking")

# Printing statements for employees

alice.welcomeEmployee()
bob.welcomeEmployee()
alice.employeeInfo()
bob.employeeInfo()

# Printing statements for parks
park01.welcome()
park02.welcome()

# Using the functions inside the park to add shops

park01.addShop("Ice Cream Parlor")
park01.addShop("Food Shoppe")
park01.addShop("Lego Land Store")

# Printing the shops we just added
park01.listShops()

# adding and then printing the employee at the park
park01.addEmployee(alice)
park01.listEmployees()