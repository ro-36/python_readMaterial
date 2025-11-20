class Car:

    totalCar = 0  # class variable

    def __init__(self, brand, model):
        Car.totalCar+=1
        self.brand = brand
        self.__model = model

    def get_brand(self):
        return self.__model

    def displayCar(self):
        print(f"Car brad: {self.__brand}, model :{self.model}")

    
class ELectricCar(Car):
    def __init__(self, brand, model, battery):
        super().__init__(brand, model)
        self.battery = battery

    

my_car = ELectricCar("Tesla", "model-X", "85Kwh")
# print(my_car.fule_type())

safari = Car("Tata", "safari")
# print(safari.fule_type())

print(Car.totalCar)