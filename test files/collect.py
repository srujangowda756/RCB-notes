from collections import Counter
l=['Apple','Banana','Mango','Orange','Mango']
data=Counter(l)
print(data)


print('==========================================')

from collections import defaultdict
d=defaultdict(int)
d['a']+=1
d['c']=23
print(d)

print('==========================================')

from collections import namedtuple
student=namedtuple('student',['name','age'])
s1=student('John',20)
print(s1)
print(s1.name)
print(s1.age)

print('==========================================')

from array import array
arr=array('i',[1,2,3,4,5])
print(arr)
arr.append(5)
print(arr)
arr.pop()
print(arr)
arr.pop(2)
print(arr)
