# Enter your code here. Read input from STDIN. Print output to STDOUTfrom abc import ABC, abstractmethod
from abc import ABC, abstractmethod
class Animal(ABC):
    def __init__(self, isMammal, isCarnivorous):
        self.isMammal = isMammal
        self.isCarnivorous = isCarnivorous
        super().__init__()

    def getIsMammal(self):
        return self.isMammal

    def getIsCarnivorous(self):
        return self.isCarnivorous

    @abstractmethod
    def getGreeting(self):
        pass


class Dog(Animal):
    def __init__(self, isMammal, isCarnivorous):
        super().__init__(isMammal, isCarnivorous)

    def getGreeting(self):
        return "Bow bow"


class Cow(Animal):
    def __init__(self, isMammal, isCarnivorous):
        super().__init__(isMammal, isCarnivorous)

    def getGreeting(self):
        return "Muh mUh"


class Duck(Animal):
    def __init__(self, isMammal, isCarnivorous):
        super().__init__(isMammal, isCarnivorous)

    def getGreeting(self):
        return "XYzX"

d = Dog(True, False)
c = Cow(True, False)
dk = Duck(False, False)

d.getIsMammal()
d.getIsCarnivorous()
d.getGreeting()



c.getIsMammal()
c.getIsCarnivorous()
c.getGreeting()

dk.getIsMammal()
dk.getIsCarnivorous()
dk.getGreeting()

