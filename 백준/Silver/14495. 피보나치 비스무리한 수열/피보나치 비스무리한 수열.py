def fib(a):
    if a < 3:
        return 1
    cnt = [0] * (a+1)
    cnt[0] = 1
    cnt[1] = 1
    cnt[2] = 1
    for i in range(3,a+1):
        cnt[i] = cnt[i-1] + cnt[i-3]
    return cnt[a-1]
a = int(input())
print(fib(a))