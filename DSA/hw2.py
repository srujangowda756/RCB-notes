# l1=[2,3,5]
# l2=[3,4,5]
# l1.extend(l2)
# print(l1)


# l1=[1,2,43,4,5,5,6]
# target=5
# count=0
# for i in l1:
#     if i==target:
#         count+=1
# print(count)


# l2={10,20,30,25,55,69,72}
# first=-1
# second=-1
# for i in l1:
#     if i>first:
#         second=first 
#         first=i
#     elif first>i>second:
#         second=i
# print(second)

# l1=[[2,3],4,[2,5],[6,7],2,'dhanush',[2]]
# result=[]
# for i in l1:
#     if type(i)==list:
#         result.extend(i)
#     else:
#         result.append(i)
# print(result)

# l1={1,2,3,4,69,69,5,6,7,8}
# temp=[]
# res=[]
# for i in l1:
#     if i in temp:
#         res.append(i)
#     else:
#         temp.append(i)
# print(res)

# print(l1.update({9,10}))
# print(l1)

# print(l1)




a=6789123
res=[]
while a>0:
    temp=a%10
    a=a//10
    res.append(temp)
n=len(res)
ans=0
res=[]
for i in range(n//2,n):
    ans=ans*10+res[i]
for i in range(n//2-1,-1,-1):
    ans=ans*10+res[i]
print(ans)

# from collections import Counter
# a='abcbdbksibasshgfdsfbverbv'
# ans=dict(Counter(a))
# print(ans)

