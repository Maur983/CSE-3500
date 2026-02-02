class Student:
    def __init__(self, grade:float):
        self.grade = grade
   
    def status(self):
        if self.grade <60:
            print("Fail")
        else:
            print("Pass")
class cseStudent(Student):
    def __init__(self, grade:float, classes:int):
        super().__init__(grade)
        self.classes = classes
    def status(self):
        if self.grade<70:
            print("Fail")
        else:
            print("Pass")
stu = cseStudent(65,5)
stu.status()
