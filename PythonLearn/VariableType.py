class Car:

    color = "Black"

    def __init__(self):
        self.mileage = 15
        self.engine = 1500
        self.brand = "Suzu"

c1 = Car()
c2 = Car()
c2.mileage = 18
c2.engine = 1200
c2.brand = "Maruti"
Car.color = "Blue"
print(c1.mileage,c1.mileage,c1.engine,Car.color)
print(c2.mileage,c2.mileage,c2.engine,Car.color)