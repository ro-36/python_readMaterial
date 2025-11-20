class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def display_car(self):# helps me establish connection with the object -- also called context  
        print(f"Car brand: {self.brand}, Model: {self.model }")
    
my_car = Car("Toyota", "Corolla")
my_car.display_car()