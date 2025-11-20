n = int (input("Enter a number:"))

sum_of_even_till_n=0

for i in range(1,n+1):
    if i%2==0:
        sum_of_even_till_n+=i
    
print(sum_of_even_till_n)
 