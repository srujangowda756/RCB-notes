# # # 1.Aarav opens a basic bank account. Later, he upgrades to a savings account, and finally to a premium savings account with extra perks.
# # # Inheritance Chain: BankAccount → SavingsAccount → PremiumSavingsAccount
# # # Class Method: Count how many accounts have been created across all levels.
# # # Static Method: Validate if an interest rate is between 0–10%.


# # class BankAccount:
# #     no_of_accounts = 0
# #     interest_rate = 3
    
# #     def __init__(self,name):
# #         self.name = name
# #         print('Basic account created')
# #         BankAccount.no_of_accounts += 1
    
# #     @classmethod
# #     def get_no_of_accounts(cls):
# #         return cls.no_of_accounts

# # class SavingsAccount(BankAccount):
# #     interest_rate = 4
# #     def __init__(self, name):
# #         print('Savings account created')
# #         super().__init__(name)
# #         BankAccount.no_of_accounts += 1

# # class PremiumSavingsAccount(SavingsAccount):
# #     interest_rate = 5
# #     def __init__(self, name):
# #         print('Premium savings account created')
# #         super().__init__(name)
# #         BankAccount.no_of_accounts += 1
    
# #     @staticmethod
# #     def validate_interest_rate(rate):
# #         return 0 < rate < 10

    
# # a=PremiumSavingsAccount('Aarav')
# # b=PremiumSavingsAccount('AaravA')
# # print(BankAccount.get_no_of_accounts())
# # print(PremiumSavingsAccount.validate_interest_rate(5))


# # # 2.	Meera joins a university as a student, then becomes a graduate student, and later a PhD candidate.
# # # Inheritance Chain: Person → Student → PhDCandidate
# # # Class Method: Count how many students are enrolled in the university.
# # # Static Method: Validate if a thesis title length is greater than 20 characters.
# # # Question: Implement the hierarchy. Use the class method to track enrollment. Use the static method to check thesis titles. Demonstrate with multiple students.

# # class Person:
# #     def __init__(self, name):
# #         self.name = name
        
# # class Student(Person):
# #     no_of_students=0
# #     def __init__(self, name, student_id):
# #         super().__init__(name)
# #         self.student_id = student_id
# #         Student.no_of_students += 1
    
# #     @classmethod
# #     def get_no_of_students(cls):
# #         return cls.no_of_students
        
# # class PhDCandidate(Student):
    
# #     def __init__(self, name, student_id,thesis_title):
# #         super().__init__(name, student_id)
# #         self.thesis_title = thesis_title
    
# #     @staticmethod
# #     def validate_thesis_title(title):
# #         return len(title) > 20
    
# #     def display_validity(self):
# #         print(f"Thesis title '{self.thesis_title}' is valid: {self.validate_thesis_title(self.thesis_title)}")


# # p=PhDCandidate('Meera',1,'AI')
# # print(Student.get_no_of_students())
# # p.display_validity()


# # # 3.	A factory produces vehicles, then cars, and finally electric cars.
# # # Inheritance Chain: Vehicle → Car → ElectricCar
# # # Class Method: Track how many cars of each type are manufactured.
# # # Static Method: Validate if a given battery capacity is realistic (>30 kWh).
# # # Question: Build the hierarchy. Use the class method to count vehicles. Use the static method to check battery capacity for electric cars.
# # class Vehicle:
# #     def __init__(self):
# #         print('Vehicle created')
        
# # class Car(Vehicle):
# #     def __init__(self):
# #         print('Car created')
# #         super().__init__()
        
# # class ElectricCar(Car):
# #     def __init__(self):
# #         print('Electric car created')
# #         super().__init__()
        




# # # 4.	A hospital has departments, and each department has doctors.
# # # Inheritance Chain: Hospital → Department → Doctor
# # # Class Method: Count total doctors across all departments.
# # # Static Method: Validate if a doctor’s license number follows a format (e.g., starts with “DOC” and has 5 digits).
# # # Question: Create the hierarchy. Use the class method to track doctors. Use the static method to validate license numbers.
# # class Hospital:
# #     def __init__(self):
# #         print('Hospital created')
        
# # class Department(Hospital):
# #     def __init__(self):
# #         print('Department created')
# #         super().__init__()
        
# # class Doctor(Department):
# #     def __init__(self):
# #         print('Doctor created')
# #         super().__init__()


# # # 5.	A customer buys products, then electronics, and finally smartphones.
# # # Inheritance Chain: Product → Electronics → Smartphone
# # # Class Method: Track total products sold.
# # # Static Method: Validate if a discount percentage is between 0–50%.
# # # Question: Implement the hierarchy. Use the class method to count sales. Use the static method to check discount validity.
# # class Product:
# #     def __init__(self):
# #         print('Product created')
        
# # class Electronics(Product):
# #     def __init__(self):
# #         print('Electronics created')
# #         super().__init__()
        
# # class Smartphone(Electronics):
# #     def __init__(self):
# #         print('Smartphone created')
# #         super().__init__()


# # # 6.	A passenger books a flight, then an international flight requiring passport validation.
# # # Inheritance Chain: Flight → PassengerFlight → InternationalFlight
# # # Class Method: Count total flights booked.
# # # Static Method: Validate if a passport number length is exactly 8 characters.
# # # Question: Build the hierarchy. Use the class method to track bookings. Use the static method to validate passport numbers.
# # class Flight:
# #     def __init__(self):
# #         print('Flight created')
        
# # class PassengerFlight(Flight):
# #     def __init__(self):
# #         print('PassengerFlight created')
# #         super().__init__()
        
# # class InternationalFlight(PassengerFlight):
# #     def __init__(self):
# #         print('InternationalFlight created')
# #         super().__init__()

# # # 7.	A library lends items, then books, and finally eBooks.
# # # Inheritance Chain: LibraryItem → Book → EBook
# # # Class Method: Track how many items are borrowed.
# # # Static Method: Validate if a file format is supported (pdf, epub).
# # # Question: Implement the hierarchy. Use the class method to count borrowed items. Use the static method to check file formats.
# # class LibraryItem:
# #     def __init__(self):
# #         print('LibraryItem created')
        
# # class Book(LibraryItem):
# #     def __init__(self):
# #         print('Book created')
# #         super().__init__()
        
# # class EBook(Book):
# #     def __init__(self):
# #         print('EBook created')
# #         super().__init__()






# # # 8.	An academy trains athletes, then runners, and finally marathon runners.
# # # Inheritance Chain: Athlete → Runner → MarathonRunner
# # # Class Method: Count how many athletes are registered.
# # # Static Method: Validate if a marathon completion time is realistic (>2 hours).
# # # Question: Build the hierarchy. Use the class method to track registrations. Use the static method to check marathon times.

# # class athletes:
# #     def __init__(self):
# #         print('athletes created')
        
# # class runner(athletes):
# #     def __init__(self):
# #         print('runner created')
# #         super().__init__()
        
# # class marathonRunner(runner):
# #     def __init__(self):
# #         print('marathonRunner created')
# #         super().__init__()

# # # 9.	A company hires employees, then developers, and finally senior developers.
# # # Inheritance Chain: Employee → Developer → SeniorDeveloper
# # # Class Method: Count total employees hired.
# # # Static Method: Validate if a programming language is in the company’s tech stack (Python, Java, C++).
# # # Question: Implement the hierarchy. Use the class method to track hires. Use the static method to validate programming languages.
# # class Employee:
# #     def __init__(self):
# #         print('Employee created')
        
# # class Developer(Employee):
# #     def __init__(self):
# #         print('Developer created')
# #         super().__init__()
        
# # class SeniorDeveloper(Developer):
# #     def __init__(self):
# #         print('SeniorDeveloper created')
# #         super().__init__()

# # # 10.	A customer places an order, then an online order, and finally an express order.
# # # Inheritance Chain: Order → OnlineOrder → ExpressOrder
# # # Class Method: Count total orders placed.
# # # Static Method: Validate if delivery time is feasible (<60 minutes).
# # # Question: Build the hierarchy. Use the class method to track orders. Use the static method to check delivery times.
# # class Order:
# #     def __init__(self):
# #         print('Order created')
        
# # class OnlineOrder(Order):
# #     def __init__(self):
# #         print('OnlineOrder created')
# #         super().__init__()
        
# # class ExpressOrder(OnlineOrder):
# #     def __init__(self):
# #         print('ExpressOrder created')
# #         super().__init__()



# class Vehicle:
#     def __init__(self):
#         enigin='yes'
        
# class Car(Vehicle):
#     def __init__(self):
#         super().__init__()
#         self.wheels=4
        
# class BMW(Car):
#     def __init__(self):
#         super().__init__()
#         self.company='BMW'
        
# e = BMW()
# print(e.wheels)




class Animal:
    def __init__(self,age):
        self.age=age

class Person(Animal):
    def __init__(self, name,age):
        super().__init__(age)
        self.name=name 

class Student(Person):
    def __init__(self, name, age,id,per):
        super().__init__(name, age)
        self.id=id
        self.per=per 
    
    def student_details(self):
        print(f"{self.name} is {self.age} years old and his ID and Percentage is {self.id} and {self.per}")

s=Student("srujan",22,1234,100)
s.student_details()
