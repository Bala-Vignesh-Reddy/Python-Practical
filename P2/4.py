# write a python program to get the frequency of the elements in a list

lst = [1, 2, 1, 3, 2, 'A', 'B', 'A']
#using list 
count = []
for i in lst:
    if i not in count:
        print(i, ":", lst.count(i))
        count.append(i)

#uses dictonary
freq = {}
for i in lst:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

print(freq)
