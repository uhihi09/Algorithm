import sys
input = sys.stdin.readline
def fib(a,b):
    cnt = [0] * (a+1)
    cnt[0] = 1 % b
    cnt[1] = 1 % b
    for i in range(2,a+1):
        cnt[i] = (cnt[i-1] + cnt[i-2]) % b
    return cnt[a-1]
n = int(input())
for i in range(1,n+1):
    a,b = map(int,input().split())
    print(f"Case #{i}: {fib(a,b)}")