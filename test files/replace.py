a='apple'
b=a.replace('p','b')
print(b)

s='python java sql'
print(s.split())

l=['Appple','orange','Mango']
print(',  '.join(l))

l3=[1,2,3,4]
print('*'.join(map(str, l3)))

s='He is at Mall'
print('is' in s)
print('or' not in s )

print(2<3 and 'Hello')
print(2>3 and 'Hello')  
print([] and 'Hi')
print({} and 'Hi')
print("" and 'Hi')  
print(0 and 'Hi')  
print(2<3 or 'Hello')
print(2>3 or 'Hello')
print(0 or 'zero')
print([] or '')

print(3<4 and 2*3)
print(False or 2+2)

print(not 0)

