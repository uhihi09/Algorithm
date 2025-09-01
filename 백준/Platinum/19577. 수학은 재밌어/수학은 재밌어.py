import math
import sys
input = sys.stdin.readline
def phi(n):
    if n == 1:
        return 1
    result = n
    for i in range(2,int(math.sqrt(n))+1):
        if n  % i == 0:
            result = result - result / i
            while n % i == 0:
                n = n / i
    if n > 1:
        result = result - result / n
    return int(result)
a = int(input())
cnt = []
ans = 0
for i in range(1,int(math.sqrt(a))+1):
    if a % i == 0:
        cnt.append(i)
        if i * i != a:
            cnt.append(a//i)
for i in cnt:
    if i * phi(i) == a:
        print(i)
        break
    else:
        ans += 1
if ans == len(cnt):
    print(-1)