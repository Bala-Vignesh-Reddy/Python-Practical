# Write a function to print default argument when it is not passed to function

def func(name = "Pragnesh"):
   # var = "Name is " + name 
    var = f"Name is {name}"
    return var  

res = func("Bala")
print(res)
