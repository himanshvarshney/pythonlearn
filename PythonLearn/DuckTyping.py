class pyCharm():
    def execute(self):
        print("Compile")
        print("Execute")

class myEditor():
    def execute(self):
        print("A stuff")
        print("Z stuff")
        print("Compile")
        print("Execute")




class Laptop():
    def coding(self,ide):
        ide.execute()
ide = myEditor()
lap = Laptop()
lap.coding(ide)