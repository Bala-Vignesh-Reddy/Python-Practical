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
