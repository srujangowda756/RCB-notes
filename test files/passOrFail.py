'''p=int(input('Enter the marks of physics '))
c=int(input('Enter the marks of chem '))
m=int(input('Enter the marks of mathe '))
b=int(input('Enter the marks of bio '))
if p<35 or c<35 or m<35 or b<35: # or if p>=35 and c>=35 and m>=35 and b>=35:
    print('Fail')
else:
    print('Pass')
'''


a=int(input('enter a '))
b=int(input('enter b '))
c=int(input('enter c '))

min=a if a<b and a<c else b if b<c else c
max=a if a>b and a>c else b if b>c else c
mid=(a+b+c)-(min+max)
print(min,mid,max)

'''
grid=[0 for i in ]'''