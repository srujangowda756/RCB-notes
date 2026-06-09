# # # # '''
# # # # Abstraction is a oop concept that hides implementaion details and shows only essential features of an object.
# # # # with the help of abstraction:
# # # #     - We can hide the internal implementation details
# # # #     - Improves core maintainability of code
# # # #     - Enforces a common interface for subclasses
# # # # '''
# from abc import ABC, abstractmethod
# # # # class Animal(ABC):
    
# # # #     @abstractmethod
# # # #     def make_sound(self):
# # # #         pass
# # # # class Dog(Animal):
# # # #     def make_sound(self):
# # # #         return "Bow Bow"
# # # # class Cat(Animal):
# # # #     def make_sound(self):
# # # #         return "Meow Meow"
# # # # d1=Dog()
# # # # c1=Cat()
# # # # print(d1.make_sound())
# # # # print(c1.make_sound())


# # # #example for interface
# # # class workabel(ABC):
# # #     @abstractmethod
# # #     def work(self):
# # #         pass

# # # class Employee(workabel):
# # #     def __init__(self,name) -> None:
# # #         self.name = name
# # #         super().__init__()
    
# # #     def meeting(self):
# # #         return "Meeting"

# # # class Tester(Employee):
# # #     def __init__(self,name,id) -> None:
# # #         super().__init__(name)
# # #         self.id = id
    
# # #     def work(self):
# # #         return "Testing"
    

# # # class Developer(Employee):
# # #     def __init__(self, name, id) -> None:
# # #         super().__init__(name)
# # #         self.id = id
    
# # #     def work(self):
# # #         return "Developing"

# # # t1=Tester("John", 1)
# # # d1=Developer("Jane", 2)
# # # print(t1.work())
# # # print(d1.work())

# # class Payment(ABC):
# #     @abstractmethod
# #     def process_payment(self):
# #         pass

# # class CreditCardPayment(Payment):
# #     def process_payment(self):
# #         return "Processing credit card payment"
    
# # class PayPalPayment(Payment):
# #     def process_payment(self):
# #         return "Processing PayPal payment"
    
# # cc=CreditCardPayment()
# # pp=PayPalPayment()
# # print(cc.process_payment())
# # print(pp.process_payment())


# class flyable(ABC):
#     @abstractmethod
#     def fly(self):
#         pass
# class swimmable(ABC):
#     @abstractmethod
#     def swim(self):
#         pass
# class Duck(flyable, swimmable):
#     def fly(self):
#         return "Duck is flying"
    
#     def swim(self):
#         return "Duck is swimming"
    
# d=Duck()
# print(d.fly())
# print(d.swim())

from abc import ABC,abstractmethod

class flyable(ABC):
    @abstractmethod
    def fly(self):
        pass
class swimmable(ABC):
    @abstractmethod
    def __swim(self):
        pass
class Duck(flyable, swimmable):
    def fly(self):
        return "Duck is flying"
    
    def _swimmable__swim(self):
        return "Duck is swimming"
    
d=Duck()
print(d.fly())
print(d._swimmable__swim())

