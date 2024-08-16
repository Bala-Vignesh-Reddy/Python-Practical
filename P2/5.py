# write a python program to find common items from two lists

lst1 = [1, 2, 'A', 5]
lst2 = [2, 'B', 'A', 4]
common = []

for i in lst1:
    if i in lst2:
        common.append(i)

print(common)

