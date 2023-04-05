'''
Python Object Definitions
-------------------------

Object Oriented programming is very structured approach to code reuse.

We can group data and functionality together and create many independant instances of a class.

Class - a template. It is not actually a thing, but shape of a thing. We define it, saying it is gonna these attributes in it these method in it.

Attribute - a variable within i class

Method - a function within a class

Object - a particular instance of a class

Constructor - code that runs when an object is created

Inheritance -
* the ability to extend a class to make a new class.
* This is a form of code reuse
* when we make a new class, we can reuse an existing class (also sub-classing) and inherit all the capabilities of an existing class and then add our own little bit to make our new class
* another form of store and reuse
* write once - reuse many times
* the new class (child) has all the capabilities of the old class (parent) - and then some more
'''


class PartyAnimal:
    x = 0
    name = ""

    def __init__(self, nam):
        self.name = nam
        print(self.name, "constructed")

    def party(self):
        self.x = self.x + 1
        print(self.name, "party count", self.x)


''' 
FoorballFan inheriting the PartyAnimal class

FoorballFan is a class which extends PartyAnimal. 
It has all the capabilities of PartyAnimal and more.
'''


class FoorballFan(PartyAnimal):
    points = 0

    def touchdown(self):
        self.points = self.points + 1
        self.party()
        print(self.name, "points", self.points)



'''
Run order;

s = PartyAnimal("Sally")
s.party()

j = FootballFan("Jim")
j.party()
j.touchdown()
'''