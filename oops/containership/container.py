# class Course:
#     def __init__(self):
#         self.cid = int(input("Enter course ID: "))
#         self.name = input("Enter course name: ")
#     def display(self):
#         print(f"Course ID: {self.cid}")
#         print(f"Course Name: {self.name}")

# class Student:
#     def __init__(self):
#         self.sid = int(input("Enter student ID: "))
#         self.name = input("Enter student name: ")
#         self.course = Course()
#     def display(self):
#         print(f"Student ID: {self.sid}")
#         print(f"Student Name: {self.name}")
#         self.course.display()

# s=Student()
# s.display()




class Dept:
    def __init__(self,dId,dname,loc):
        self.dId=dId
        self.dname=dname
        self.loc=loc
        
    def display_details(self):
        print(f"In the {dname} with {dId} and its located in {self.loc}")
    
class Emp:
    def __init__(self,eid,name,des,sal,dId,dname,loc):
        self.eId=eid
        self.name=name
        self.designation=des 
        self.sal=sal 
        self.department=Dept(dId,dname,loc)
    def display_emp_details(self):
        print(f"The employee {self.name} with id {self.eId} is working as {self.designation} with salary {self.sal}")

e=Emp(1,"srujan","Backend developer",500000,2,"Development","Bengaluru")
e.display_emp_details()

print("--------------------------------------")

class Address:
    def __init__(self,city,state,country):
        self.city=city 
        self.state=state 
        self.country=country
    
    def display(self):
        print("city Name",self.city)
        print("state name",self.state)
        print("country name",self.country)

class Customer:
    def __init__(self,name,mob,address):
        self.name=name 
        self.mob=mob 
        self.address=address
    
    def customer_details(self):
        print("Customer Name",self.name)
        print("Customer Mobile",self.mob)
        self.address.display()

add1=Address("Bengaluru","Karnataka","India")
add2=Address("Hyderabad","Telangana","India")
cust1=Customer("Srujan",9876543210,add1)
cust1.customer_details()
cust2=Customer("Rahul",9876543210,add2)
cust2.customer_details()