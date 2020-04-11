from abc import ABC, abstractclassmethod

class Computer(ABC):
    @abstractclassmethod
    def screen(self):
        pass
    def backlit(self):
        print("No")


class Laptop(Computer):

    def screen(self):
        print("14 inches")
    def show(self):
        pass


comp = Laptop()
comp.screen()
comp.backlit()
comp.show()

