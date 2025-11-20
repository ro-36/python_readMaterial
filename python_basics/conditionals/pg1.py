a = int(input("Enter a number: "))
if a < 13:
    print("Child")
elif a>=13 and a<19:
    print("Teenager")
elif a>=20 and a<60:
    print("Adult")
else:
    print("Senior Citizen")