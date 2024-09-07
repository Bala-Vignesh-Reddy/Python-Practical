# Write a function to append [11,22,33] to the existing list

def append_list(lst):
    lst.append([11,22,33])
    return lst

l1 = [1,2,3]
updatedLst = append_list(l1)
print(updatedLst)
