class Car:
    # init is also a constructor like in C++
    def __init__(self, brand, model): # self is a reference to the current instance of the class just like this in C++
        self.brand = brand # self is important even if paramater name that we use is different from attribute name
        self.model = model

my_car = Car("Toyota", "Corolla")
print(my_car.brand)  # This will raise an AttributeError
print(my_car.model)  # This will raise an AttributeError