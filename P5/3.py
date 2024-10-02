<<<<<<< HEAD
# Write a function to print default argument when it is not passed to function

def func(name = "Pragnesh"):
   # var = "Name is " + name 
    var = f"Name is {name}"
    return var  

res = func("Bala")
print(res)
=======
# Write a function to print default argument when it is not passed to function

def greet(name="Bala"):
    print("Hello, " + name + ", how do you do!!")

greet() # print with default argument
greet("Dax") #argument is given to the function
>>>>>>> 9f37ad3 (P5)
