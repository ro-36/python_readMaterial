def genEven_no(num):
    for i in range (1, num + 1):
        if i % 2 == 0:
            print(i)
    # for i in range (2, num + 1, 2):
    #     print(i)

genEven_no(20)

## using yield ---> generator function
# -- this helps u to generate the values one by one instead of storing all the values in the memory at once
print("using yield")
def genEven_yield(num):
    for i in range (1, num + 1):
        if i % 2 == 0:
            yield i
for i in genEven_yield(10):
    print(i)