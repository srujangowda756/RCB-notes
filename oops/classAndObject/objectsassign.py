class Employee:
    def __init__(self,ename,sal):
        self.ename=ename
        self.sal=sal
    def printInfo(self):
        print(self.ename,self.sal)
a=Employee('shashu',1000)
a.printInfo()
b=a
b.sal=200
a.printInfo()
b.printInfo()


class Pen:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    def __del__(self):
        print("object is deleted")
    
p1=Pen('meow',50)
p1.color='red'
print(p1.__dict__)

def displayPenDetails():
    print("hello")
    
p1.showPenDetails = displayPenDetails
p1.showPenDetails()

#print(dir(p1))
'''
for i in dir(p1):
    print(i)


import math
print(dir(math))

for i,j in vars(math).items():
    print(i,j)
'''
e1=Employee("PG",123456789)
e1.printInfo()