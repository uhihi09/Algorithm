def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        sum = 0
        a,b = 0,1
        for i in range(n-1):
            sum = a+b
            a = b
            b = sum
        return sum
a = int(input())
print(fib(a))