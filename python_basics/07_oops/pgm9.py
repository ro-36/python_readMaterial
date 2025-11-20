class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.__model = model

    def get_brand(self):
        return self.__model

    def displayCar(self):
        print(f"Car brad: {self.__brand}, model :{self.model}")

    def fule_type(self):
        return "Petrol or Disele"
    
class ELectricCar(Car):
    def __init__(self, brand, model, battery):
        super().__init__(brand, model)
        self.battery = battery

    def display(self):
        print(f"Car: {self.get_brand()}, model: {self.model}, battery: {self.battery}")
    
    def fule_type(self):# polymorphism
        return "Electricity"
    

my_car = ELectricCar("Tesla", "model-X", "85Kwh")
print(isinstance(my_car, Car))
print(isinstance(my_car, ELectricCar))


safari = Car("Tata", "safari")
print(isinstance(safari, Car))
print(isinstance(safari, ELectricCar))
# print(safari.fule_type())