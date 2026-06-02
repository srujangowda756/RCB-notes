class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
student = Student("John", 20)

file=open('student.pkl', 'wb')

import pickle

pickle.dump(student, file)