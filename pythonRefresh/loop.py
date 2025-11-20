# # # # # # n= int(input("Enter a number: "))
# # # # # # for i in range(n,(n*10)+1,n):
# # # # # #     print(f"{n} *{i//n} = {i}")

# # # # # n= int(input("Enter a number: "))
# # # # # fact =1
# # # # # for i in range(1,n+1):
# # # # #     fact *=i

# # # # # print("Factorial=", fact)

# # # # n= int(input("Enter a number: "))
# # # # odd_sum =0
# # # # even_sum=0
# # # # for i in range(n+1):
# # # #     if(i%2==0):
# # # #         even_sum +=i
# # # #     else:
# # # #         odd_sum +=i
    
# # # # print("Odd Sum =", odd_sum) 
# # # # print("Even Sum =", even_sum)


# # # n= int(input("Enter a number: "))
# # # print("Factors of", n, "are:")
# # # for i in range(1,n+1):
# # #     if(n%i==0):
# # #         print(i)

# # n= int(input("Enter a number: "))
# # sum = 0
# # for i in range(1,n):
# #     if(n%i==0):
# #         sum+=i

# # if sum == n :
# #     print(n, "is a perfect number")


# s = "hello"
# for i in range(len(s)-1, -1, -1):
#     print(s[i])

str = "P@#yn26at^&i5ve"
char = 0
num = 0
spchar = 0

for i in str:
    if i.isalpha():
        char += 1
    elif i.isdigit():
        num += 1
    else:
        spchar += 1

print("Characters =", char)
print("Numbers =", num)
print("Special Characters =", spchar)