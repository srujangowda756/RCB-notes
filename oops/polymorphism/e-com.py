
    
class Upi:
    def pay(self,amount):
        print(f"pay {amount} with upi")

class CreditCard:
    # def pay(self,amount):
    #     self.amount = amount
    #     print(f'pay {self.amount} with credit card')
    pass 
class DebitCard:
    def pay(self,amount):
        print(f'pay {amount} with debit card')

class CashOnDelivery:    
    def pay(self,amount):
        print(f'Pay {amount} when parcel arrives')

def payments(obj,amount):  
    obj.pay(amount)

u=Upi()
payments(u,100)

#use of get attribute

c=CreditCard()
setattr(c,'pay',lambda amount: print(f'pay {amount} with credit card'))
payments(c,200)
