class Animal:
    def speak(self):
        print("I am an animal")

class Dog(Animal):  # Inherits from Animal
    def speak(self):
        print("Woof Woof 🐶")

class Cat(Animal):
    def speak(self):
        print("Meow 🐱")

dog = Dog()
cat = Cat()
dog.speak()
cat.speak()