# class Student:
#     college_name='IISC-Bangalore'
#     def info(self, id, name, percentage):
#         self.id=id
#         self.name = name
#         self.percentage = percentage
#     def print_info(self):
#         print(f'ID: {self.id}, Name: {self.name}, Percentage: {self.percentage}, College: {self.college_name}')
# s1=Student()
# s1.info(1,'John',90)
# s1.print_info()
# s2=Student()
# s2.info(2,'Jane',95)
# s2.print_info()



# class Student:
#     def __init__(self, id, name, percentage):
#         self.id=id
#         self.name = name
#         self.percentage = percentage
#     def __str__(self):
#         return f'ID: {self.id}, Name: {self.name}, Percentage: {self.percentage}'
#     def __del__(self):
#         print(f"Student object with id {self.id} deleted")

# s1=Student(1, "John", 90)
# s2=Student(2, "Jane", 99)
# print(s1)
# print(s2)

#this is know as magic methods
#define emp class overload all the relational operators to compare the slaray between two employee  
class employee:
    def __init__(self,name,sal):
        self.name=name
        self.sal=sal 
    def __gt__(self,other):
        return self.sal>other.sal

    def __eq__(self,other):
        return self.sal==other.sal

    def __le__(self,other):
        return self.sal<other.sal
    def __ne__(self,other):
        return self.sal!=other.sal
    
a=employee('a',500)
b=employee('b',600)
print(a>b)  
print(a==b)  
print(a<b)     
print(a!=b)     
