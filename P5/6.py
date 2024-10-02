# Write a python function that accepts a string and calculate the number of uppercase letters and lowercase letters

str1 = "HelloWorld"
lower = 0
upper = 0
for i in str1:
    if(i.islower()):
        lower += 1
    else:
        upper += 1
print("Lowercase letters:", lower)
print("Uppercase letters:", upper)
