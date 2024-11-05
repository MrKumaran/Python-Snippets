"""
Efficient method for finding the nth Fibonacci number

fib_eff is faster one(more memory)
Fibonacci is slower one(more time)
"""

import time as t


def fib_eff(n):
    fib =[0, 1]
    if n == 0:
        return fib
    elif n == 1:
        return fib
    else:
        for _ in range(2, n+1):
            fib.append(fib[-1] + fib[-2])
        return fib[-1]


def Fibonacci(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)


n = int(input())
start = t.time()
fibi = fib_eff(n)
end = t.time()
print(fibi)
print("Time taken: ", end-start)
start = t.time()
fibi = Fibonacci(n)
end = t.time()
print(fibi)
print("Time taken: ", end-start)
