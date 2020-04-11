class Student:
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()

    def show(self):
        print(self.name,self.rollno)
        self.lap.show()

    class Laptop:
        def __init__(self):
            self.brand="HP"
            self.cpu = "i5"
            self.ram = "8GB"
        def show(self):
            print(self.brand,self.cpu,self.ram)


s1 = Student('Himanshu',20)

lap1 = Student.Laptop()
#print(s1.name,s1.rollno)
s1.show()