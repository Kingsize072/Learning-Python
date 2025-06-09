class Student:
    studentStatus = "Active"
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
student1 = Student("CheeZe", 4)
print(Student.studentStatus)