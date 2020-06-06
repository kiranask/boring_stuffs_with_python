# Python program showing
# abstract class cannot
# be an instantiation
from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def move(self):
        pass


c = Animal()