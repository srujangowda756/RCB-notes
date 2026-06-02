players=['Kohli','ronaldo','verstappen']
numbers=[18,7,3]
sports=['Cricket','Football','F1']
s=zip(players,numbers,sports)

print(s)

print('================================================')

print(list(s))
for i,j,k in zip(players,numbers,sports):
    print(i,j,k)

print('================================================')

sports=['Cricket','Football']
for i,j,k in zip(players,numbers,sports):
    print(i,j,k)

print('================================================')

from itertools import zip_longest
for i,j,k in zip_longest(players,numbers,sports,fillvalue='Not Given'):
    print(i,j,k)

print('================================================')

l=[1,2,3,4]
a,b,c,d=l
print(a,b,c,d)

print('================================================')

l=[1,2,3,4]
a,b,*c=l
print(a,b,c)

print('================================================')

l=[1,2,3,4]
*a,b=l
print(a,b)

print('================================================')

s={1,2,3}
s.add(4)
s.update({5,6})
print(s)
s.remove(6)
print(s)
s.discard(5)
print(s)

print('================================================')
sa={1,2,3,4}
for i,j in enumerate(sa,start=0):
    print(i,j)

print('================================================')

sa={1,2,3,4}
sa=frozenset(sa)
print(sa)# cant add or remove elements from frozenset

print('================================================')

s1={1,2,3,4,5,6}
s2={4,5,6,7,8}
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))
print(s1.symmetric_difference(s2))
s3={1,2,3}
print(s3.issubset(s1))
print(s1.issuperset(s3))
print(s1.isdisjoint(s3))