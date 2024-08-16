#write a python program to remove an empty tuple(s) from a list of tuples

lst = [(1, 2, 3), (), ('a', 'b', 'c'), (), (2,)]
ans = []

for i in lst:
    if i:
        ans.append(i)

print(ans)
