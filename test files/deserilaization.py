import pickle
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
# open the file in binary mode
with open('student.pkl', 'rb') as file:
    # load the student object from the file
    student = pickle.load(file)

# print the age and name of the student
print(student.age)
print(student.name)