class Student:

    # initialise functions
    # usually custom attributes added after the default 'self' attribute
    # this is basically a student data type which all the attributes associated with it
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

    # function within a class
    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False
