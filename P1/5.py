# Write a program to add the number stored in array till the counter reaches to user defined counter

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
count = int(input("Enter the count:"))
sum1 = 0
for i in range(count):
    sum1 += arr[i]
print("Sum: ", sum1)
