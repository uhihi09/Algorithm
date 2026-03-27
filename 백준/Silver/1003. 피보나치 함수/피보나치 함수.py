import sys
input = sys.stdin.readline
def fib(n):
    f = [0] * (n+1)
    if n > 0:
        f[1] = 1
        for i in range(2,n+1):
            f[i] = f[i-1] + f[i-2]
    return f[n]
def fib2(n):
    f = [0] * (n+1)
    f[0] = 1
    if n > 0:
        for i in range(2,n+1):
            f[i] = f[i-1] + f[i-2]
    return f[n]
a = int(input().strip())
for i in range(a):
    b = int(input())
    print(fib2(b), fib(b))