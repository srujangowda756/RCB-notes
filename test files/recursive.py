def rec(i):
    if i==10:
        return
    print(i)
    rec(i+1)
rec(1)

import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())
#rec(1)
print('================================================')

import random
print(random.randint(1,10))

print('================================================')

l=[1,2,4,5,6,7,8,9,10]
print(random.choice(l))
print(random.choices(l,k=2))
print(random.sample(l,k=2))
print(random.random())