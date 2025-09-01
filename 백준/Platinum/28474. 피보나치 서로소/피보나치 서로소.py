import math
def phi(n):
    result = n
    if n == 1:
        return 0
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            result = result - result // i
            while n % i == 0:
                n = n // i
    if n > 1:
        result = result - result // n
    return int(result)
a = int(input())
for i in range(a):
    b = int(input())
    if b % 2 == 0:
        print(phi(b)+phi(b//2))
    else:
        print(phi(b))