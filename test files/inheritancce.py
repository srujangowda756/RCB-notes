class Mother:
    def __init__(self):
        self.color="White"
        self.age=21

class Father:
    def __init__(self):
        self.height=180
        self.age=23 
    
class Son(Mother,Father):    #multiple inheritance ---->

    def __init__(self):
        Mother.__init__(self)
        Father.__init__(self)

s=Son()
print(s.color,s.height)   


#===========================================================================
class Employee:
    def __init__(self):
        print("Devloper is created")


class Devloper(Employee):
    def __init__(self,name):
        super().__init__()
        self.name=name
    def role(self):
        print(self.name,"is a Devloper")
d=Devloper("John")
d.role()

#=============================================
#Access Specifier
#page=public
#_page=protected
#__page=private

#=============================================
class Book:
    def __init__(self):
        self.__pages=100
        self._price=100
        self.pages=100
b=Book()
print(b.pages)
print(b._price)
#print(b.__pages)  ## will give you error so you need to add a getter method

class Book:
    def __init__(self):
        self.__pages=100
        self._price=100
        self.pages=100
    def get_pages(self):
        print(self.__pages)
    def setter(self,pages):
        self.__pages=pages
b=Book()
b.get_pages()
b.setter(200)
b.get_pages()

#==================================================================
class Book:
    def __init__(self):
        self.__pages=100
    @property
    def pages(self):
        return self.__pages
    @pages.setter
    def pages(self,pages):
        self.__pages=pages
b=Book()
b.pages=200
print(b.pages)

#==================================================================

class Circle:
    pi=3.14
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return self.pi*self.radius*self.radius
c1=Circle(3)
print(c1.area())

#==================================================================
import os
print(os.getcwd())