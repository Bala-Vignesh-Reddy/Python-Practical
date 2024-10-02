# Write a Python program to call function inside function.

def greet(name):
    return "Hello, " + name

def message(name):
    greeting = greet(name)
    return greeting + "! Welcome to the seminar."

name = input("Enter name:")
print(message(name))
