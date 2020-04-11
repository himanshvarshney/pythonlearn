class Computer:
    def __init__(self):
        self.name = "Himanshu"
        self.age = 28
    def compare(self,other):
        if self.age == other.age:
            print("They are same")
        else:
            print("They are different")

c1 = Computer()
c2 = Computer()
c2.name = "Varshney"
c2.age = 29

c1.compare(c2)
print(c1.name,c1.age," C2 ", c2.name,c2.age)