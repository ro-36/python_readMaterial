class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_car(self):
        print(f"Car company: {self.brand} model: {self.model}")
    
class ElectricCar(Car):# inherits car
    def __init__(self, brand, model, batterySize):
        super().__init__(brand, model)
        self.batterySize = batterySize


my_tesla = ElectricCar("Tesla", "model-X", "85Kwh")
my_tesla.display_car()