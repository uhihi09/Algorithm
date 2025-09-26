def fib(a):
    if a < 1:
        return 1
    cnt = [0] * (a+1)
    cnt[0] = 1
    cnt[1] = 1
    for i in range(2,a+1):
        cnt[i] = (cnt[i-1] + cnt[i-2]+1) % 1000000007
    return cnt[a]
a = int(input())
print(fib(a))