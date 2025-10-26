#Class oops
class Student():
    def __init__(self, name, grade):
        self.name = name 
        self.grade = grade

    def student_details(self):
        print(f"{self.name} is in class {self.grade}")       


student1 = Student("Ankit", "Bachelors_1stsem")
print(student1.name)
student1.student_details()
