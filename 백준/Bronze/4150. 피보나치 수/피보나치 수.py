import sys
input = sys.stdin.readline
def fib(a):
    if a < 2:
        return 1
    else:
        cnt = [0] * (a+1)
        cnt[1] = 1
        cnt[2] = 1
        for i in range(3,a+1):
            cnt[i] = cnt[i-1] + cnt[i-2]
        return cnt[a]
a = int(input())
print(fib(a))