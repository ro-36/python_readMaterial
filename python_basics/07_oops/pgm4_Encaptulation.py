class Car:
    def __init__(self, brand, model):
        self.__brand = brand # im making brand private .. and this can only be accessed within the class with the variable name
        self.model = model

    def get_brand(self):
        return self.__brand

    def displayCar(self):
        print(f"Car brad: {self.__brand}, model :{self.model}")

class ELectricCar(Car):
    def __init__(self, brand, model, battery):
        super().__init__(brand, model)
        self.battery = battery

    def display(self):
        print(f"Car: {self.get_brand()}, model: {self.model}, battery: {self.battery}")
    

my_car = ELectricCar("Tesla", "model-X", "85Kwh")
my_car.displayCar()
my_car.display()