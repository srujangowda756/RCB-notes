def number():
    yield 1
    yield 2
    yield 3

gen=number()
print(type(gen))
print(next(gen))
print(next(gen))
print(next(gen))

print('====================================================')

l=[1,2,3,4]
it=iter(l)
print(type(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))


gen=(x for x in range(1000))
print(gen)