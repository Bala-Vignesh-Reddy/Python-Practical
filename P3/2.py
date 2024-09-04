#write a program that removes all occurrence of a given letter from string.

str1 = "Python Programming"

char = input("Enter the character:")

for i in str1:
    if char in str1:
        str1 = str1.replace(char, '')        

print(str1)
