# WAP to get Fibonacci series between 0 to 50

a = 0
b = 1

def fibo(n):
    if n < 0:
        print("Invalid Input")
    elif n==0:
        return a
    elif n==1:
        return b

    return fibo(n) + fibo(n+1)

ans = fibo(10)
print(ans)
