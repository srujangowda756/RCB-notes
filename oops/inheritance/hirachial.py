# # # # class Father:
# # # #     def home(self):
# # # #         print("This is father's home")
# # # # class son1(Father):
# # # #     def home(self):
# # # #         print('This is son1 home')

# # # # class son2(Father):
# # # #     def home(self):
# # # #         print('This is son2 home')

# # # # s=son1()
# # # # s.home()

# # # # s2=son2()
# # # # s2.home()

# # # #what is the constructor in oops?
# # # #constructor is a special method that is called when an object is created
# # # #constructor is used to initialize the object
# # # #constructor is optional
# # # #constructor is not required to return any value
# # # #constructor is not required to have a name
# # # #constructor is not required to be unique
# # # #constructor is not required to be defined in the class
# # # #constructor is not required to be called explicitly
# # # #constructor is not required to be inherited
# # # #constructor is not required to be overridden
# # # #constructor is not required to be overloaded
# # # #constructor is not required to be static
# # # #constructor is not required to be final
# # # #constructor is not required to be abstract
# # # #constructor is not required to be private
# # # #constructor is not required to be protected
# # # #constructor is not required to be public
# # # #constructor is not required to be default
# # # #constructor is not required to be parameterized
# # # #constructor is not required to be copy constructor
# # # #constructor is not required to be move constructor
# # # #constructor is not required to be delegating constructor
# # # #constructor is not required to be inheriting constructor
# # # #constructor is not required to be user-defined constructor
# # # #constructor is not required to be compiler-generated constructor
# # # #constructor is not required to be default constructor
# # # #constructor is not required to be parameterized constructor
# # # #constructor is not required to be copy constructor
# # # #constructor is not required to be move constructor
# # # #constructor is not required to be delegating constructor
# # # #constructor is not required to be inheriting constructor
# # # #constructor is not required to be user-defined constructor
# # # #constructor is not required to be compiler-generated constructor

# # # # class vehical:
# # # #     def __init__(self):
# # # #         pass
# # # #     def display(self, type, brand, color):
# # # #         print(f'This is {type} of {brand} with color {color}')

# # # # class car(vehical):
# # # #     def __init__(self,type, brand, color):
# # # #         self.type = type
# # # #         self.brand = brand 
# # # #         self.color = color
# # # #     def display(self):
# # # #         super().display(self.type, self.brand, self.color)

# # # # class truck(vehical):
# # # #     def __init__(self,type, brand, color):
# # # #         self.type = type
# # # #         self.brand = brand 
# # # #         self.color = color
# # # #     def display(self):
# # # #         super().display(self.type, self.brand, self.color)

# # # # # Test the classes
# # # # c = car("car", "BMW", "red")
# # # # c.display()

# # # # t = truck("truck", "Tata", "blue")
# # # # t.display()

# # # class Food:
# # #     def __init__(self,name):
# # #         self.name=name

# # # class Biriyani(Food):
# # #     def __init__(self,name,item1,item2,item3):
# # #         super().__init__(name)
# # #         self.item1 = item1
# # #         self.item2 = item2
# # #         self.item3 = item3
# # #     def display(self):
# # #         print(f'This is {self.name} with ingredients {self.item1}, {self.item2}, {self.item3}')

# # # class Cake(Food):
# # #     def __init__(self,name,item1,item2,item3):
# # #         super().__init__(name)
# # #         self.item1 = item1
# # #         self.item2 = item2
# # #         self.item3 = item3
# # #     def display(self):
# # #         print(f'This is {self.name} with ingredients {self.item1}, {self.item2}, {self.item3}')

# # # b = Biriyani('Biriyani',"rice", "spices", "onion")
# # # b.display()

# # # c = Cake('Cake',"flour", "sugar", "eggs")
# # # c.display()



# # class Student:
# #     def __init__(self,name,age):
# #         self.name = name
# #         self.age = age

# # class Engineering(Student):
# #     def __init__(self,name,age,college):
# #         super().__init__(name, age)
# #         self.college = college

# # class CSE(Engineering):
# #     def __init__(self,name,age,college,subject):
# #         super().__init__(name, age, college)
# #         self.subject = subject
    
# #     def display(self):
# #         print(f'This is {self.name} with college {self.college} and subject {self.subject}')

# # class Mech(Engineering):
# #     def __init__(self,name,age,college,subject):
# #         super().__init__(name, age, college)
# #         self.subject = subject
    
# #     def display(self):
# #         print(f'This is {self.name} with college {self.college} and subject {self.subject}')

# # cs=CSE("John", 20, "RV College", "Math")
# # cs.display()

# # mech=Mech("Jane", 22, "RV College", "Physics")
# # mech.display()



# # #Access specifier
# # #Public - accessible from anywhere, defined like self.varname
# # #Private - accessible only within the class ,defined like self.__varname
# # #Protected - accessible within the class and its subclasses, defined like self._varname


class Crop:
    count=0
    def __init__(self):
        Crop.count+=1
    @staticmethod
    def pH(num):
        return 7<num<=14        

class Wheat(Crop):
    pass

class Rice(Crop):
    pass
class Corn(Crop):
    pass

crop1=Wheat()
crop2=Rice()
crop3=Corn()

print(Crop.count)
print(crop1.pH(3))


class Shipment:
    count=0
    def __init__(self):
        Shipment.count+=1
    @classmethod
    def count_shipment(cls):
        return cls.count       

class DomesticShipment(Shipment):
    
    pass

class InternationalShipment(Shipment):
    pass

d=DomesticShipment()
i=InternationalShipment()
print(Shipment.count_shipment())
