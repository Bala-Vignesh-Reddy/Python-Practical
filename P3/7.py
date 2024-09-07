#Write a python program which takes two digits m(row) and n
#(column) as input and generates a two-dimensional array .The
#element value in the i-th row and j-th column of the array should be
#i*j
def arr(m, n):
    arr1 = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(i*j)
        arr1.append(row)
    return arr1

m = int(input("Enter rows:"))
n = int(input("Enter columns:"))

res = arr(m, n)
print("Generated 2D Array")
for i in res:
    print(i)
