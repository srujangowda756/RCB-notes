# simple example of polymorphism
class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

# Usage
animals = [Dog(), Cat()]
for animal in animals:
    print(animal.make_sound())

#what is polymorphism?
#polymorphism is the ability of an object to take on many forms
#in python, polymorphism refers to the way in which different object classes can share the same method name, and those methods can be called from the same place even though a variety of different objects might be passed in
#polymorphism is the ability of an object to take on many forms
#in python, polymorphism refers to the way in which different object classes can share the same method name, and those methods can be called from the same place even though a variety of different objects might be passed in