class Animal:
    # jsdgc
    # jhsdcgj
    pass


class Dog(Animal):
    # Constructor: initializes object properties
    def __init__(self, name, breed, age):
        self.name = name      # 'self' refers to the current object
        self.breed = breed
        self.age = age

    # Method to make dog bark

    def bark(self):
        return f"{self.name} is barking! Woof 🐶"


    # Method to show dog details
    def show_details(self):
        return f"Name: {self.name}, Breed: {self.breed}, Age: {self.age}"


dog1 = Dog("Hatchi","Pom", 8)

print(dog1.bark())


