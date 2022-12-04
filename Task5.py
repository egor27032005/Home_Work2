fib1 = fib2 = 1
 
n = int(input())
for i in range(2, n):
    fib1, fib2 = fib2, fib1 + fib2

fib2=fib2*(-1)
print(fib2, fib1, end=' ')
for i in range(2,n):
    fib2, fib1=fib1, fib1+fib2
    print(fib1, end = " " )

fib1 = fib2 = 1
print(0, fib1, fib2, end=' ')
for i in range(2, n):
    fib1, fib2 = fib2, fib1 + fib2
    print(fib2, end = " " )