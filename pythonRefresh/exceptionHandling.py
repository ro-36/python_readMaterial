a = int(input("Enter a number :"))

try:
    q = 10/a
except Exception as e:
    print("Cannot be performed",e)
else:
    print("Good there is no exception")
finally:
    print("Good idc i will run anyway")

print("Ok i have done this division")


# raise Exception("This is an exception")

age = int(input("Enter your age : "))
if age<10 or age>18:
    raise ValueError("Age must be between 10 and 18")
else:
    print("Welcome to the club")