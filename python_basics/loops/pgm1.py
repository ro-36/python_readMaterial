numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
positive_number_counter =0

for i in numbers:
    if(i>0):
        positive_number_counter+=1
print(f"Final count of +ve number is= {positive_number_counter}")