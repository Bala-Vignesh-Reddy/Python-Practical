<<<<<<< HEAD
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
=======
# Write a function to return the sum of two number. Defined sum as global and local variable and see the difference

#as a global variable 
sum1 = 0
def add1(a,b):
    sum1 = a+b
    print("Global Sum:", sum1)
    return sum1 
print("Global returned ans:", add1(4,5))

#as a local variable
def add(a, b):
    sum = a+b
    print("Local sum:", sum)
    return sum

ans = add(5,6)
print("Returned Ans:", ans)
>>>>>>> 9f37ad3 (P5)
