class Circle:
    pi=3.14
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return self.pi * self.radius * self.radius
    def perimeter(self):
        return 2 * self.pi * self.radius
    def __add__(self,other):
        return self.radius + other.radius
    def __sub__(self,other):
        return self.radius - other.radius
    def __mul__(self,other):
        return self.radius * other.radius
    def __truediv__(self,other):
        return self.radius / other.radius
    def __floordiv__(self,other):
        return self.radius // other.radius
    def __mod__(self,other):
        return self.radius % other.radius
    def __pow__(self,other):
        return self.radius ** other.radius
c1=Circle(5)
c2=Circle(10)
print(c1+c2)
print(c1-c2)
print(c1*c2)
print(c1/c2)
print(c1//c2)
print(c1%c2)
print(c1**c2)
