# a special type of method that is available only to class and is not available to instant
class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model

    def get_brand(self):
        return self.__brand

    def displayCar(self):
        print(f"Car brad: {self.__brand}, model :{self.model}")

    def fule_type(self):
        return "Petrol or Disele"
    

    @staticmethod # this is called decorators 
    def general_discription():
        return "cars are means of transport" # removing self itself is enough but @ static is preffarable
    
    @property # will not let any new setting to variable
    def model(self):
        return self.__model

class ELectricCar(Car):
    def __init__(self, brand, model, battery):
        super().__init__(brand, model)
        self.battery = battery

    def fule_type(self):# polymorphism
        return "Electricity"
    

my_car = ELectricCar("Tesla", "model-X", "85Kwh")

car = Car("Tata", "safari")
print(car.model)
# car.model="Corola"
print(car.model)

