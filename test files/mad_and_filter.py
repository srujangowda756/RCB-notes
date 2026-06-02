def add(i):
    return i+10
s=[1,2,3,4,5,6,7,8,9,10]
res=list(map(add,s))
print(res)

def is_even(i):
    return i%2==0

res=list(filter(is_even,s))
print(res)

def is_divisible_by_3(i):
    return i%3==0

res=list(filter(is_divisible_by_3,s))
print(res)



