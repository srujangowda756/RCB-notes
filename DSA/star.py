n=5
for i in range(n):
    print("* " *n)

print('===========1==============')

for i in range(n):
    print("* " *i)
print('============2=============')
for i in range(1,n):
    print(" " * (n-i) +"* " *i)
for i in range(n,0,-1):
    print(" " * (n-i) +"* " *i)
print('============3=============')

for i in range(1,n):
    print("* " * i+' '*(4*(n-i))+'* ' * i)


for i in range(n,0,-1):
    print("* " * i+' '*(4*(n-i))+'* ' * i)

print('============4=============')

for i in range(1,n):
    print(" " * (n-i-1),end=" ")
    for j in range(1,i):
        if j == 1 or j == i-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
for i in range(n,0,-1):
    print(" " * (n-i),end='')
    for j in range(1,i):
        if j==1 or j==i-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

print('==========5============')


for i in range(n,0,-1):
    print('* '*i)

print('===========6==============')

for i in range(1,n):
    for j in range(1,i+1):
        print(j,end=' ')
    print()

print('============7=============')

for i in range(1,n+1):
    for j in range(1,i+1):
        print(f'{i},{j}',end=' ')
    print()
print('============8=============')

k=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(k,end=' ')
        k+=1
    print()

print('============9=============')

for i in range(1,n+1):
    k=i
    for j in range(1,i+1):
        print(k,end=' ')
        k+=1
    print()
print('=============10============')

for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(j+64),end=' ')
    print()

print('=============11=============')
for i in range(1,n+1):
    for j in range(1,n+1):
        print(j%2,end=' ')
    print()
print('=============12=============')
for i in range(1,n+1):
    for j in range(1,n+1):
        print(i%2,end=' ')
    print()
print('=============13=============')
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end=' ')
    print()
print('=============14=============')
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end=' ')
    print()
print('===========15==============')
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(j,end=' ')
    print()

print('===========17==============')
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i%2,end=' ')
    print()
print('===========18==============')
for i in range(1,n+1):
    for j in range(n,i-1,-1):
        print(j,end=' ')
    print()
print('==========19==========')
for i in range(n):
    for j in range(n):
        if i%2==0 and j%2==0:
            print(1,end=' ')
        else:
            print(0,end=' ')
    print()
print('============20===============')
for i in range(n):
    for j in range(1,n+1):
        print((i+j)%2,end=" ")
    print()
print('============21============')
for i in range(1,n+1):
    print("  "*(n-i)+("* "*(i)))
print('============22============')
for i in range(1,n+1):
    print("  "*(n-i)+(2*i-1)*"* ")
print('============23============')
for i in range(n,0,-1):
    print("  "*(n-i)+(2*i-1)*"* ")
print('============24==========')
for i in range(n,0,-1):
    print("  "*(n-i)+("* "*(i)))

# import os
# import time
# for i in range(1,n+20):
#     os.system('cls')
#     for j in range(1,n+1):
#         print(' '*3*i+"  "*(n-j)+(2*j-1)*"* ")
#     time.sleep(1)
print('===============25=================')
for i in range(n,0,-1):
    print("  "*(n-i),end='')
    for j in range(i,0,-1):
        print(j,end=' ')
    print()

print('==============26==================')
for i in range(n,0,-1):
    print("  "*(n-i),end='')
    for j in range(1,i+1):
        print(j,end=' ')
    print()
print('=============27==================')

for i in range(1,n+1):
    print("  "*(n-i),end='')
    for j in range(i,0,-1):
        print(j,end=' ')
    print()

print('=============28==================')

for i in range(1,n+1):
    print("  "*(n-i),end='')
    for j in range(1,i+1):
        print(j,end=' ')
    print()
print('=============29=================')
for i in range(1,n+1):
    print(" "*(n-i),end='')
    for j in range(n,n-i,-1):
        print(j,end=' ')
    print()
print('===========30============')
for i in range(n,0,-1):
    print(" "*(n-i),end='')
    for j in range(n,n-i,-1):
        print(j,end=' ')
    print()
print('========31===========')
for i in  range(n,0,-1):
    print("  "*(i-1),end='')
    for j in range(n,i-1,-1):
        print(j,end=' ')
    print()
print('=========32==========')

for i in range(1,n+1):
    print('  '*(n-i),end="")
    for j in range(1,2*i):
        print(j%2,end=' ')
    print()
    
print('=========33==========')
for i in range(1,n+1):
    print("  "*(n-i)+"* "*i)
print('=========34==========')
for i in range(1,n+1):
    print("  "*(n-i),end="")
    for j in range(1,i+1):
        if j==i:
            print(j,end='')
        else:
            print(f'{j} * ',end='')
    print()
print('=========35==========')

for i in range(1,n+1):
    print('  '*(n-i),end='')
    for j in range(1,i):
        print(j,end=' ')
    for j in range(i,0,-1):
        print(j,end=' ')
    print()

print('==============36================')

for i in range(1,n+1):
    print("  "*(n-i),end='')
    x=i
    for j in range(1,2*i):
        print(x,end=' ')
        if j<i:
            x-=1
        else:
            x+=1
    print()

print('=========37==========')
for i in range(1,n+1):
    x=i
    print("  "*(n-i),end='')
    for j in range(1,i+1):
        print(x,end=' ')
        x+=1
    print()

