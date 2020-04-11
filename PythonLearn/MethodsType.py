class Student:
    school = "Lovely"

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1+self.m2+self.m3)/3

    @classmethod
    def info(cls):
        return cls.school

    @staticmethod
    def classInfo():
        print("Static Method")


s1=Student(46,78,69)
s2=Student(69,79,78)


print(s1.avg())
print(Student.school)
Student.classInfo()