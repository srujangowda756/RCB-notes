class Animal:
    def eat(self):
        pass
    def sleep(self):
        pass
    def drink(self):
        pass 

class Deer(Animal):
    def eat(self):
        print('Deer will graze')
    def sleep(self):
        print('Deer is sleeping')


d=Deer()
d.eat()
d.sleep()
d.drink()