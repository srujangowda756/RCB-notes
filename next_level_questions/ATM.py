class ATM:
    def __init__(self,id,name,balance,pin):
        self.id=id
        self.name=name
        self.balance=balance
        self.pin=pin
    def verify_pin(self,temp):
        if temp==self.pin:
            return True
        else:
            return False
    def deposite(self,amount):
        temp=int(input("Enter your pin to deposite"))
        if self.verify_pin(temp):
            self.balance+=amount
            print(f'Amount deposite successful, your new balance is {self.balance}')
        else:
            print("Invalid pin")
    def withdraw(self,amount):
        temp_pin=int(input("Enter your pin to withdraw "))
        if self.verify_pin(temp_pin):
            if self.balance>=amount:
                self.balance-=amount
                print(f'Amount withdraw successful, your new balance is {self.balance}')
                print('Please collect your cash')
            else:
                print('Insufficient balance')
        else:
            print("Invalid pin")
    
    def check_balance(self):
        temp_pin=int(input("Enter your pin to check your balance"))
        if self.verify_pin(temp_pin):
            print('Your balance is',self.balance)
        else:
            print("Invalid pin")

a=ATM(123,'John',1000,1234)
a.withdraw(500)


        

