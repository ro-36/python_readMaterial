num = int(input("Enter a number: "))

fact = 1
print(f"Factorial of {num} is :")

while num > 0:
    fact = fact*num
    num = num -1

print(fact)