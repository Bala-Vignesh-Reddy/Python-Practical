# write a python program that accepts a string and calculates the number of digits and letters

str1 = input("Enter a string:")

digit = letter = 0 

for i in str1:
    if i.isnumeric():
        digit += 1
    elif i.isalpha():
        letter += 1

print("Digits:", digit)
print("Letters:", letter)
