class Person:
    def __init__(self, name):
        self.name = name
    # To get name

    def getName(self):
        return self.name
    # To check if this person is employee
# This Implementation will get lost.
    def isEmployee(self):
        return False


# Inherited or Sub class (Note Person in bracket)
class Employee(Person):

    # Here we return true
    def isEmployee(self):
        return True
# Driver code
emp = Person("Geek1")  # An Object of Person
print(emp.getName(), emp.isEmployee())
emp = Employee("Geek2")

print(emp.getName(), emp.isEmployee())
