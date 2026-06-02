from turtle import heading


class calc:
    def add(self,a,b):
        print(a+b)
    def add(self,a,b,c):
        print(a+b+c)

obj=calc()
obj.add(10,20,30)   # this is method overaiding


class calc:
    def add(self,a,b,c=0):
        print(a+b+c)

obj=calc()
obj.add(10,20)   # this is method overloading


class Number:
    def __init__(self,num):
        self.num=num
    def __add__(self, other):
        return 'Addition overloaded'
    def __sub__(self, other):
        return 'Subtraction overloaded'
    def __mul__(self, other):
        return 'Multiplication overloaded'
    def __truediv__(self, other):
        return 'Division overloaded'
    def __mod__(self, other):
        return 'Modulo overloaded'
    def __floordiv__(self, other):
        return 'Floor division overloaded'
a=Number(5)
b=Number(6)
print(a-b)
print(a+b)
print(a*b)
print(a/b)
print(a%b)
print(a//b)


#over Raiding

class Animal:
    color='Black'
    height=10
    no_of_legs=4 
    def Shout(self):
        print("Animal is shouting")

class Dog(Animal):
    def Shout(self):
        print('Dog is barking')

class Lion(Animal):
    def Shout(self):
        print('Lion is roaring')

d=Dog()
d.Shout()
l=Lion()
l.Shout()
