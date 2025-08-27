class Animal:
    def speak(self):
        print("I am an animal")

class Dog(Animal):  # Inherits from Animal
    def speak(self):  # Overrides parent's method
        print("Woof Woof 🐶")

class Cat(Dog):
    def speak(self):  # Overrides parent's method
        print("Meow 🐱")

dog = Dog()
cat = Cat()
animal = Animal()

dog.speak()  # Woof Woof 🐶
cat.speak()
animal.speak()
