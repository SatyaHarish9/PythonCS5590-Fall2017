# Airports class
class Airports:
    # Constructor
    def __init__(self, aname, city):
        self.aname = aname
        self.city = city


# Creating instance of Airport class
a1 = Airports("ABC", "hyderabad")
a2 = Airports("MCI", "kansas")


# Flight class with flight details
class Flight:
    # Constructor
    def __init__(self, flightnum, flightname):
        self.flightnum = flightnum
        self.flightname = flightname

    def displayFlights(self):
        print("Flight number :" + str(self.flightnum), "Flight name: " + self.flightname)


# Creating instance of Flight class
f1 = Flight(350, "Emirates")
f2 = Flight(250, "Delta")


# Employee class with details
# Employee has multiple inheritance. It inherits the properties of Airports and Flight classes.
class Employee(Airports, Flight):
    # Constructor
    def __init__(self, first, last, airportName, flname, flnum):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@gmail.com'
        #Use of Multiple Inheritance
        Airports.aname = airportName
        Flight.flightname = flname
        Flight.flightnum = flnum
        #Calling method of Parent class
        Flight.displayFlights(self)

    def employeeDisplay(self, airportName, flname):
        print("First name:" + self.first, "Last name:" + self.last)

        # Creating instance of Employee class


emp1 = Employee("harish", "gumpalli", "MCI", "Delta", 2315)
emp2 = Employee("abhiram", "nalla", "RGI", "Eithad", 3562)
emp1.employeeDisplay("MCI","Emirates")
emp2.employeeDisplay("RGI","Eithad")


# Passenger class inheriting the properties of Airports and Flight
class Passenger(object):
    # Constructor
    def __init__(self, fname, lname, contact, price, ticktype):
        self.fname = fname
        self.lname = lname
        self.contact = contact
        self.price = price
        self.ticktype = ticktype
        print("Passengers class includes the details of passengers about to board")

    def displayPassenger(self):
        print("Passenger First name:" + self.fname, "Passenger Last name:" + self.lname, "Ticket price:" + str(self.price))

    #definition of a private member
    def __priva(self):
        print("I am Private Passenger")

# Creating instance of Passenger class
p1 = Passenger("sachin", "tendulkar", 9973188763, 1500, "business")
p1._Passenger__priva

# Tickets class inheriting Passenger class
class Tickets(Passenger):
    # Constructor
    def __init__(self, fname, lname, contact, price, ticktype):
        # Use of super keyword to call the method in parent class
        super(Tickets, self).__init__(fname, lname, contact, price, ticktype)
        print("Tickets class inherits the properties of Passenger Class")

    def ticketDisplay(self):
        print("Ticket price:" + str(self.price), "Ticket type:" + self.ticktype)


# Creating instance of Tickets Class
t1 = Tickets("Virat", "Kohli", 9843162641, 1500, "economy")
print(t1.displayPassenger())