# write a python program to check whether a list contains a sublist

lst = [1, 2, [3, 4], ['a', 'b']]
lst1 = [3, 4] # for checking

if lst1 in lst:
    print("It contains sublist")
else:
    print("It doesn't contain sublist")
