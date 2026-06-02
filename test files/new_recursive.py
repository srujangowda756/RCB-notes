def po(b,p):
    if p==0:
        return 1
    return b*po(b,p-1)
print(po(2,3))

print('=============================================')

def isPrime(n):
    if n<=1:
        return False
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True
print(isPrime(11))

print('=============================================')

for i in range(1,100):
    if isPrime(i):
        print(i)


print('=============================================')

def amstrong(tot,n,p):
    if len(tot)==11:
        return tot
    temp=0
    for i in range(n):
        temp+=int(i)*p
    if temp==int(n):
        tot.append(temp)
    amstrong(tot,str(int(n)+1),p)

tot=[]
n='1'
amstrong(tot,n,len(n))


print('=============================================')