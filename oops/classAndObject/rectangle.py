class Rectangle:
    def __init__(self, length,bredth):
        self.length = length
        self.bredth= bredth
    def area(self):
        return self.bredth * self.length
    def perimeter(self):
        return 2*(self.length+self.bredth)
    def __add__(self,other):
        return f'length:{self.length+other.length} bredth:{self.bredth+other.bredth}'
    def __sub__(self,other):
        return f'length:{self.length-other.length} bredth:{self.bredth-other.bredth}'
    def __mul__(self,other):
        return f'length:{self.length*other.length} bredth:{self.bredth*other.bredth}'
    def __truediv__(self,other):
        return f'length:{self.length/other.length} bredth:{self.bredth/other.bredth}'
    def __floordiv__(self,other):
        return f'length:{self.length//other.length} bredth:{self.bredth//other.bredth}'
    def __gt__(self,other):
        return self.area()>other.area()
    def __lt__(self,other):
        return self.area()<other.area()
    def __eq__(self,other):
        return self.area()==other.area()
    def __ne__(self,other):
        return self.area()!=other.area()

r1=Rectangle(2,5)
r2=Rectangle(4,8)
print(r1+r2)
print(r1-r2)
print(r1*r2)
print(r1/r2)
print(r1//r2)
print(r1>r2)
print(r1<r2)
print(r1==r2)
print(r1!=r2)

#dunder methods are special methods which are prefixed and suffixed with double underscores