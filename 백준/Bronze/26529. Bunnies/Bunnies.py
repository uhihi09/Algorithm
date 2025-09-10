a = int(input())
def fib(n):
    if n == 0:
        return 1
    cnt = [0] * (n+1)
    cnt[0] = 1
    cnt[1] = 1
    for i in range(2,n+1):
        cnt[i] = cnt[i-1] + cnt[i-2]
    return cnt[n]
for i in range(a):
    b = int(input())
    print(fib(b))