# WAP to get Fibonacci series between 0 to 50

a = 0
b = 1

#print(a, end=" ")
while b <= 50:
 #   print(b, end=" ")
    a,b = b, a + b

def fibo(n):
    if n < 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

n=0 
print(0, 1, end=" ")
while 1:
    fib = fibo(n)
    if fib > 50:
        break
    print(fib, end=" ")
    n +=1

#print(fibo(5))
