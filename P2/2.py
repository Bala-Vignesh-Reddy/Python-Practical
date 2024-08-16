# WAP to remove duplicates from the list

lst1 = [1, 2, 3, 1, 2, 5]
lst2 = []

for i in lst1:
    if i not in lst2:
        lst2.append(i)

print(lst2)
