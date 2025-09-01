import math
a = int(input())
ans = 0
for ii in range(1,a+1):
    result = ii
    n = ii
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            result = result - result / i
            while n % i == 0:
                n = n / i
    if n > 1:
        result = result - result / n
    ans += result
print(int(ans)-1)