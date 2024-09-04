#WAP to print the start pattern using nested for loop

for i in range(5):
    print("*" * i)

for j in range(5, 0, -1):
    print("*" * j)


"""rows = int(input("Enter the number of rows: "))

for i in range(0, rows):
    for j in range(0, i ):
        print("*", end=' ')
    print()

for i in range(rows , 0, -1):
    for j in range(1, i - 1):
        print("*", end=' ')
    print()
"""
