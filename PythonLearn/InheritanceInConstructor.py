class A:
    def __init__(self):
        print("In A init")

    def feature1(self):
        print("In feature 1-A")
    def feature2(self):
        print("In feature 2-A")

class B(A):
    def __init__(self):

        print("In B init")
        super().__init__()


    def feature3(self):
        print("In feature 3-B")
    def feature4(self):
        print("In feature 4-B")

b=B()
b.feature1()