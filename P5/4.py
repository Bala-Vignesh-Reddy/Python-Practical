# Write a function to return the sum of two number. Defined sum as global and local variable and see the difference
def sum(a, b):
    local_sum = a + b
    global global_sum 
    global_sum = a + b
    print("Local Sum:", local_sum)
    return local_sum

a = int(input("Enter first number:"))
b = int(input("Enter second number:"))

res = sum(a,b)
print("Returned value:", res)
print("Global Sum:", local_sum)