# Iterator is a object that can be iterated over

my_list = [1,2,3,4,5,6,7,8,9,10]
my_iterator = iter(my_list)
print(next(my_iterator))
print(next(my_iterator))    


#same thing using while loop

while True:
    try:
        print(next(my_iterator))
    except StopIteration:
        break

print('====================================================================')


#using class
class Counter:
    def __init__(self,limit):
        self.limit=limit 
        self.cur=0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.cur<self.limit:
            self.cur+=1
            return self.cur
            
        else:
            raise StopIteration 
a=Counter(10)
for val in a:
    print(val)

print('======================')
b=Counter(10)
while True:
    try:
        value=next(b)
        print(value)
    except StopIteration:
        break

