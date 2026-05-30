"""
class_and_object.py
Principal SDET Python Interview Prep

TOPIC:
Classes and Objects in Python

GOAL:
By reading comments alone, you should understand:
- what is a class
- what is an object
- why OOP exists
- how Python creates objects internally
- what self means
- constructor behavior
- memory model
- interview insights
"""



# ==========================================================
# WHAT IS A CLASS?
# ==========================================================

# CLASS:
# A blueprint/template for creating objects.
#
# Think:
# Architectural drawing of a house.
#
# The blueprint itself is NOT the real house.
#
# Similarly:
# class definition is NOT an actual object.
#
# It only describes:
# - what data objects will have
# - what behavior objects will have


class Car:

    # ======================================================
    # CONSTRUCTOR
    # ======================================================

    # __init__ is called automatically
    # when object gets created.
    #
    # Purpose:
    # initialize object state.

    def __init__(self, brand, color):

        # self:
        # reference to CURRENT object.
        #
        # Python automatically passes it.
        # These are instance variable

        self.brand = brand
        self.color = color

        # RESULT after assignment:
        #
        # object will contain:
        #
        # brand = value
        # color = value

    # ======================================================
    # METHOD
    # ======================================================

    # Method = function inside class.

    def start(self):

        # self.brand:
        # access current object's brand

        print(f"{self.brand} started")

    def paint(self):
        # self.color
        print(f"color of the CAR is {self.color}")


# ==========================================================
# IMPORTANT:
# NO OBJECT YET
# ==========================================================

# At this point:
#
# ONLY blueprint exists.
#
# No actual car created.
#
# Memory:
#
# Car class definition exists in memory
#
# But:
# no individual object.


# ==========================================================
# WHAT IS AN OBJECT?
# ==========================================================

# OBJECT:
# Real instance created from class.
#
# Think:
# Actual house built using blueprint.


# Object Creations

bmw = Car("BMW", "Black")
benz = Car("BENZ", "White")

# WHAT PYTHON DOES INTERNALLY:
#
# Step 1:
# Allocate memory for new object.
#
# Step 2:
# Create empty Car instance.
#
# Step 3:
# Automatically call:
#
# Car.__init__(bmw, "BMW", "Black")
#
# IMPORTANT:
#
# Python automatically passes:
# self = current object reference
#
# Step 4:
# Store attributes inside object.


# ==========================================================
# MEMORY VISUALIZATION
# ==========================================================

# Memory conceptually:
#
# bmw --------------+
#                   |
#                   v
#              Car Object
#             +------------+
#             | brand=BMW |
#             | color=Blk |
#             +------------+


# ==========================================================
# OBJECT RESULT
# ==========================================================

# RESULT:
#
# bmw.brand = "BMW"
# bmw.color = "Black"


# ==========================================================
# ACCESS OBJECT DATA
# ==========================================================

brand_name = bmw.brand
color_car = bmw.color
print(f"Brand Name is {brand_name}")
print(f"Color of the car is  {color_car}")

# WHAT PYTHON DOES:
#
# 1. Look inside object
# 2. Find attribute "brand"
# 3. Return stored value

# RESULT:
#
# brand_name = "BMW"


# ==========================================================
# METHOD CALL
# ==========================================================

bmw.start()
bmw.paint()
# WHAT PYTHON DOES:
#
# Converts internally:
#
# Car.start(bmw)
#
# self automatically becomes:
#
# self = bmw object

# OUTPUT:
#
# BMW started


# ==========================================================
# MULTIPLE OBJECTS
# ==========================================================

audi = Car("Audi", "White")

# IMPORTANT:
#
# audi is COMPLETELY separate object.

# MEMORY:
#
# bmw -----------> Car Object 1
#
# audi ----------> Car Object 2

# RESULT:
#
# bmw.brand  = BMW
# audi.brand = Audi


# ==========================================================
# INSTANCE VARIABLES
# ==========================================================

# self.brand
# self.color
#
# These belong to EACH object separately.
#
# Example:
#
# bmw.brand  != audi.brand


# ==========================================================
# CLASS VARIABLES
# ==========================================================

class Employee:

    # CLASS VARIABLE
    #
    # Shared by ALL objects.
    #
    # Stored once at class level.

    company = "Akamai"

    def __init__(self, name):

        # INSTANCE VARIABLE
        #
        # Separate per object

        self.name = name


e1 = Employee("Kiran")
e2 = Employee("Rahul")

# RESULT:
#
# e1.company = Akamai
# e2.company = Akamai
#
# Shared variable.

# But:
#
# e1.name = Kiran
# e2.name = Rahul


# ==========================================================
# DIFFERENCE:
# CLASS vs OBJECT
# ==========================================================

# CLASS:
#
# Blueprint/template.
#
# OBJECT:
#
# Actual instance created using class.


# ==========================================================
# REAL AUTOMATION FRAMEWORK EXAMPLE
# ==========================================================

# In Selenium framework:
#
# LoginPage
# DashboardPage
# APIClient
#
# are CLASSES.
#
# Actual runtime objects:
#
# login_page = LoginPage(driver)
#
# are OBJECTS.


# ==========================================================
# WHY CLASSES IMPORTANT?
# ==========================================================

# Benefits:
#
# 1. Reusability
# 2. Maintainability
# 3. Encapsulation
# 4. Better organization
# 5. Scalable architecture


# ==========================================================
# INTERVIEW TRICK QUESTION
# ==========================================================

# QUESTION:
#
# Does class consume memory?
#
# YES.
#
# Class object itself exists in memory.
#
# But object memory gets allocated
# when instances are created.


# ==========================================================
# INTERVIEW ANSWER
# ==========================================================

"""
Class:
Blueprint defining attributes and behavior.

Object:
Runtime instance created from class.

self:
Reference to current object instance.

__init__:
Constructor used for object initialization.

Instance Variables:
Unique per object.

Class Variables:
Shared across all objects.
"""


# ==========================================================
# MEMORY TRICK
# ==========================================================

"""
CLASS
= blueprint

OBJECT
= real thing

self
= current object

__init__
= object initializer
"""
"""

What is instance variable:

self.name
self.salary
self.driver

Variable inside the inside the constructor or methods, belongs to individual  object,

Class Variable:

belongs to the class,
One copy per class , Shared across all the objects..


"""