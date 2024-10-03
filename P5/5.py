# write a python program to reverse the string using function and while loop

def rev(s):
    rev1 = ""
    i = len(s) - 1
    while i>=0:
        rev1 += s[i]
        i -= 1
    return rev1 

str1 = input("Enter the string:")
print("Entered string:", str1)
print("Reversed String:", rev(str1))


