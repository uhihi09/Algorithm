import math
while True:
    a = int(input())
    result = a
    n = a
    if n == 0:
        break
    if n == 1:
        print(0)
        continue
    for i in range(2,int(math.sqrt(a))+1):
        if n % i == 0:
            result = result - result // i
            while n % i ==0:
                n = n // i
    if n > 1:
        result = result - result // n
    print(int(result))