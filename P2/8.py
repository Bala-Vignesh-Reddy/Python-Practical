# write a python program to check whether a list contains a sublist

lst = [1, 2, [3, 4], ['a', 'b']]
lst1 = [1, 2, 3] # for checking
ans = False
for i in lst1:  # change the list name to check
    if type(i) == list:
        ans = True

if ans == True:
    print("It contains sublist")
else:
    print("It doesn't contain sublist")
