# def print_details(name, power):
#     print(f"Name: {name}")
#     print(f"Power: {power}")

# print_details(name = "saktiman", power="lazer eye")

# but the above one may not be use in the case we want to pass multipal arguments so we follow the bellow approach of kwargs

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")

print_kwargs(name="Alice", age=30, city="New York")