# # class Animal:
# #     def speaks(self):
# #         print('Animal make sound')

# # class Dog(Animal):
# #     def eat(self):
# #         print('Dog eats meat')


# # d=Dog()
# # d.eat()
# # d.speaks()


# class Base_account:
#     def __init__(self,account_number,balance=50000):
#         self.account_number=account_number
#         self.balance=balance

#     def deposite(self,amount):
#         self.balance+=amount
#         print('Amount deposite successful')
#         print(f'the current balance is {self.balance}')
    
#     def withdraw(self,amount):
#         if self.balance>=amount:
#             self.balance-=amount
#             print('withdraw successful')
#         else:
#             print('Check the balance')
#         print('the current balance is {self.balance}')
        
# class Saving_account(Base_account):
#     def display_intrest(self):
#         interest=(self.balance*12*3)/100
#         print(f'The interest for a year is {interest}')
    
# s=Saving_account(1234,10000)
# s.deposite(30000)
# s.display_intrest()

class Parent:
    def __init__(self):
        self.name='Parent'
class Child(Parent):
    def __init__(self):
        print("Child class")
c=Child()

#parent class construtor wont run automatically if child has its own constructor 
# you have to use super to do that 

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print("Parent class")
class Student(Person):
    def __init__(self,name,age,id,per):
        super().__init__(name,age)
        self.id=id
        self.per=per
    def studentInfo(self):
        print("name",self.name)
        print("age",self.age)
        print("ID",self.id)
        print("Percentage",self.per)
        print("----------------------")

c=Student("sru",22,12334,100)
s=Student("s",23,12335,99)
c.studentInfo()
s.studentInfo()


#method over raiding: A child class can redefine super class method 