# a = 25652
# b = a
# rev = 0
# while(b>0):
#     r = b%10
#     rev = rev *10 +r
#     b//=10

# if rev == a:
#     print("palandrome")
# else:
#     print("Not palandrome")

import random 

num = random.randint(1,11)
tries = 0

while True:
    guess = int(input("Pleas guess the number b/w 1 and 10 : "))
    tries +=1
    if num == guess:
        print(f"You are correct, number of takes taken {tries}")
        break
    else :
        print("You are wrong")
        