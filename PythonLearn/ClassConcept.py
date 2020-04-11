class Laptop:
    def __init__(self,cpu,ram,hd):
        self.cpu = cpu
        self.ram = ram
        self.hd =hd

    def system(self):
        print(self.cpu,self.ram,self.hd)

HP = Laptop("i5","8GB","1TB")
Dell = Laptop("i7","16GB","512GB")



HP.system()
Dell.system()
