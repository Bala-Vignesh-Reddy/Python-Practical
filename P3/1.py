# take integer input from user until user presses q. Print average and product of all numbers.
# brute force method there can be more effective method also!!!

# using only one variable
avg = sum1 = count = 0
prod = 1
while True:
    num = input("Enter the number,  Press q to exit!! : ")
    if num == 'q':
        break
    else:
        sum1 += int(num)
        prod *= int(num)
        count += 1 

print("Average:", sum1/count)
print("Product:", prod)

# using list 
lst = []
count = 1
"""
while True:
    num = input("Enter the number,  Press q to exit!! : ")
    if num == 'q':
        break
    else:
        lst.append(int(num))

avg = sum1/count
#print(lst)
for i in lst:
    sum1 += i
    prod *= i
    count += 1
avg = sum1/count
#print(avg)
"""
