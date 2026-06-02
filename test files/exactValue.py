from decimal import Decimal
from fractions import Fraction
import math

a=1/6
print(Decimal(1/3)) 

print(Decimal(a))

print(Fraction(1,3))

print(Fraction(0.5))

print(math.pi)  


r=3
print("Area of circle is in decimal",Decimal(math.pi*r*r))
print("Circumference of circle is in decimal",Decimal(math.pi*2*r))  

print("Floor value of 4.8 is ",math.floor(4.8))
print("Ceil value of 4.8 is ",math.ceil(4.8))
print("e is ",math.e) #e value  
print("Square root of 4 is ",math.sqrt(4))
print("Power of 2 to 3 is ",math.pow(2,3))

print("LCM of 2 and 3 is ",math.lcm(2,3))
print("GCD of 12,48 and 30 is ",math.gcd(12,48,30))
print("Factorial of 5 is ",math.factorial(5))

a=5 
def outer():
    a=10
    print(a)
    def inner():
        nonlocal a
        a=15
        print(a)
    inner()
    print(a)
outer()
print(a)


print('name \b age')
print(r'yes\no')                  


h='Hello World'
print(h.lower())
print(h.upper())
print(h.capitalize())
print(h.title())


print(h.startswith('h'))
print(h.endswith('d'))