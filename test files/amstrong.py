def power(b,e):
    return b**e
def is_amstrong(n):
    total=0
    n=len(str(n))
    for i in str(n):
        total+=power(int(i),n)
    return total 
StartNum=int(input("Enter a number: "))
EndNum=int(input("Enter another number: "))
for i in range(StartNum,EndNum+1):
    if i==is_amstrong(i):
        print(i)
    
