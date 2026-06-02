a=[1,2,3]
b=[1,2,3]

print(a==b)
print(a is b)

print(2<3)
print(4>1)
print(4<=4)
print(5>=2)# bro this are relational operators
print(5!=2)

#Logical operators
print(2>3 or 4>5)
print(2<3 and 4<5)
print(not 0)

#bit wise operator

print(1 & 0)  #bit wise and
print(1 | 0)  #bit wise or
print(1 ^ 0)  #bit wise xor
print(~3)     #bit wise not
print(3 << 2)   #left shift formula x * 2**n
print(2 >> 1)   #right shift formula ceil(x / 2**n)

#Presidence

#PEMDAS
#Parentheses
#Exponents
#Multiplication
#Division
#Addition
#Subtraction
print((2*3)**4+1/2)
print(2*3**4+1/2)

from functools import reduce

def mul(x,y):
    return x*y
l=[6,3,2,8,1]
print(reduce(mul,l))

def div(n,m):
    return n/m

l1=[18,3,2]
print(reduce(div,l1))


print(list(map(lambda x: x**2, l)))

print(reduce(lambda x,y: x*y, l))


x= lambda a: a%2==0
print(x(5))
print(x(48))

y=lambda a:a%5==0
print(y(10))
print(y(12))

age=20
i=1
print('can vote' if age>18 else 'cannot vote' )
print('Holiday' if i==1 else 'workday' if i==0 else'Invalid input' )

def greet():
    print("How are you")
    
def add_name(name, func):
    print(f"Hello {name}")
    func()
add_name('srujan',greet)
