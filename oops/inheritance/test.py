print('===================1========================')
class Account:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient balance")
    
class SavingsAccount(Account):
    
    def add_interest(self):
        self.balance += (self.balance *3*12)/100
        print(f'The interest will be {(self.balance *3*12)/100}')
    
s = SavingsAccount(1234, "virat", 1000)
s.deposit(1000)
s.add_interest()

print('===================2========================')


class Patient_base:
    def __init__(self, name, age,medical_history):
        self.name = name
        self.age = age
        self.medical_history = medical_history

class Patient_Sub(Patient_base):
    def __init__(self, name, age, medical_history, room_num,daily_charge):
        super().__init__(name, age, medical_history)
        self.room_num = room_num
        self.daily_charge = daily_charge 
    
    def total_charge(self, days):
        return f'The total charge is {self.daily_charge * days}'

p=Patient_Sub("max", 30, "Diabetes", 101, 1500)
print(p.total_charge(7))

print('====================3=======================')

class Vehical:
    def __init__(self,v_no,fule_cap,milage=25):
        self.v_no=v_no
        self.fule_cap=fule_cap
        self.milage=milage
class Car(Vehical):
    def trip_charge(self,distance):
        return f'the cost of trip considering fule is Rs 100 per liter is Rs {distance / self.milage * 100}'

c=Car(1234,50,25)
print(c.trip_charge(500))


print('====================4=======================')

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

class EBook(Book):
    def __init__(self, title, author, price, pdf_size,discount):
        super().__init__(title, author, price)
        self.pdf_size = pdf_size
        self.discount = discount
    
    def final_price(self):
        return f'The final price after discount is {self.price - (self.price * self.discount / 100)}'

e = EBook("Introduction to c", "Dennis richie", 400, "10MB", 10)
print(e.final_price())

print('====================5=======================')


class menuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class combo(menuItem):
    def __init__(self,items):
        self.items = items
    
    def total_price(self):
        total=0
        for item in self.items:
            total += item.price
        print('total price is',total)

item1=menuItem("Item 1", 120)
item2=menuItem('item 2',150)
item3=menuItem('item 3',200)

c = combo([item1, item2, item3])
c.total_price()


print('====================6=======================')

class Course:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration
class Online_course(Course):
    def __init__(self, name, duration, platform,fee):
        super().__init__(name, duration)
        self.platform = platform
        self.fee = fee
    
    def avg_cost(self,no_of_students):
        return f'The average cost per student is {self.fee / no_of_students}'

oc = Online_course("Introduction to Python", 12, "Coursera", 100000)
print(oc.avg_cost(50))

print('====================7=======================')

class product:
    def __init__(self, productId, price,stock):
        self.productId = productId
        self.price = price
        self.stock = stock
    
class Discounted_product(product):
    def __init__(self, productId, price, stock, discount):
        super().__init__(productId, price, stock)
        self.discount = discount
    
    def final_price(self):
        return f'The final price after discount is {self.price - (self.price * self.discount / 100)}'

p=Discounted_product("Product 1", 2000, 10, 15)
print(p.final_price())

print('====================8=======================')


class Movie:
    def __init__(self, title, duration,rating):
        self.title = title
        self.duration = duration
        self.rating = rating
    
class Streaming_movie(Movie):
    def __init__(self, title, duration, rating, platform,cost_per_hour):
        super().__init__(title, duration, rating)
        self.platform = platform
        self.cost_per_hour = cost_per_hour
    
    def total_cost(self):
        return f'The total cost is {self.cost_per_hour * self.duration}'

m1 = Streaming_movie("Dhurandhar", 2.5, 5, "Netflix", 50)
print(m1.total_cost())

print('====================9=======================')

class Hotel:
    def __init__(self,room_number,price_per_night):
        self.room_number = room_number
        self.price_per_night = price_per_night

class DulexRoom(Hotel):
    def __init__(self, room_number, price_per_night,extra_service):
        super().__init__(room_number, price_per_night)
        self.extra_service = extra_service
    
    def total_cost(self, no_of_nights):
        return f'The total cost for {no_of_nights} nights is {self.price_per_night * no_of_nights + self.extra_service}'
    
d = DulexRoom("Room 1", 2000, 1500)
print(d.total_cost(3))

print("==================10===============")

class Emp:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Emp):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus
    
    def total_salary(self):
        return f'The total salary is {self.salary + self.bonus}'

m = Manager("Pradeep", 50000, 10000)
print(m.total_salary())
