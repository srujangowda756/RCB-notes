# from keyword import kwlist
# print(kwlist)
# print("Total keywords:", len(kwlist))
# print('==========================')
# a=10
# print(id(a))
# b=10
# print(id(b)) 


a=1257
print(id(a))
b=1257
print(id(b))
print('==========================')

m,n=500,500
print(id(m))
print(id(n))

#binary begins with 0b
#octal begins with 0o
#hexadecimal begins with 0x
#decimal may have numbers between 0-9 but should not start with 0


#int consumes 28bytes in memory
#float consumes 24bytes in memory
#complex consumes 32bytes in memory
#bool consumes 28bytes in memory
#str consumes 49bytes in memory

import sys
print('int:',sys.getsizeof(10000000000))
print('float:',sys.getsizeof(10.5))
print('complex:',sys.getsizeof(10+5j))
print('bool:',sys.getsizeof(True))
print('str:',sys.getsizeof("hellooooooooo"))