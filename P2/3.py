# write a python function that takes two lists and returns tur if they have at leat one common member

def check(lst1, lst2):
    for i in lst1:
        if i in lst2:
            return True
    return False

lst1 = [1, 2, 3, 4]
lst2 = [5, 7, 1, 6]

checking = check(lst1, lst2)
print(checking)
