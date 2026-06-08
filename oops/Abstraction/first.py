'''
Abstraction is a oop concept that hides implementaion details and shows only essential features of an object.
with the help of abstraction:
    - We can hide the internal implementation details
    - Improves core maintainability of code
    - Enforces a common interface for subclasses
'''
from abc import ABC, abstractmethod
class Animal(ABC):
    
    @abstractmethod
    def make_sound(self):
        pass
class Dog(Animal):
    def make_sound(self):
        return "Bow Bow"
class Cat(Animal):
    def make_sound(self):
        return "Meow Meow"
d1=Dog()
c1=Cat()
print(d1.make_sound())
print(c1.make_sound())

