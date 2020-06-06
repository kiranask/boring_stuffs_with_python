# Python code to demonstrate how parent constructors
# are called.

# parent class
class Person(object):

    # __init__ is known as the constructor / here parent constructor
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print(self.name)
        print(self.idnumber)

# child class

class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post

        # invoking the __init__ of the parent class
        Person.__init__(self, name, idnumber)

    # creation of an object variable or an instance


a = Person('Rahul', 886012)

# calling a function of the class Person using its instance
a.display()

b = Employee('Kiran',18521,2400000,'Snr. SDET', )
b.display()