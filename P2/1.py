# WAP to create list and tuple with different data types and show the difference between list and tuple 

lst1 = [1, "Hi", True, "How do you do", 0.2]
print(lst1)

lst1[1] = "Change" # list are mutable so we can change values
print(lst1)

tup1 = (1, "hi", False, "Kuch bi", 20.1)
tup1[1] = "No" #error because tuple are immutable so we cannot change value
print(tup1)
