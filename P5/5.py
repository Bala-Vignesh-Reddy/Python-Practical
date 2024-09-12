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