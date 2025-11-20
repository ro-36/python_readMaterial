a = int(input("Enter a number: "))
day = input("Enter day:")

price = 12 if a >=18 else 8

if day == "W" or "w":
    price -=2

print(f"Ticket price for is : ${price}")
