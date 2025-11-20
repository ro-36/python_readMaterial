num = int(input("Enter a number :"))

if num < 2:
    print(f"number {num} is not prime")
else :
    for i in range (2, (num//2)+1):
        if (num%i) == 0:
            print(f"number {num} is not prime")
            break
    else:
        print(f"number {num} is prime")