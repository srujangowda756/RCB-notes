# encaptulation in python is not possible beacuse we can access the private variable and methods of a class from outside the class
# but we can achieve it by using private methods and variables

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __private_method(self):
        print("This is a private method")
    
    def public_method(self):
        print("This is a public method")
        self.__private_method()

s = Student("John", 20)
s.public_method()


# python is not 100% oops oriented programing language because encapsulation fails even when we use 
# (__) strong private methods and variables
