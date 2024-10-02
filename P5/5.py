<<<<<<< HEAD
# write a python program to reverse the string using function and while loop

def reverse_string(string):
    reversed_string = ""
    index = len(string) - 1
    
    while index >= 0:
        reversed_string += string[index]
        index -= 1
    
    return reversed_string

# Example usage
original_string = input("Enter a string: ")
reversed_result = reverse_string(original_string)

print("Original string:", original_string)
print("Reversed string:", reversed_result)
=======
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


>>>>>>> 9f37ad3 (P5)
