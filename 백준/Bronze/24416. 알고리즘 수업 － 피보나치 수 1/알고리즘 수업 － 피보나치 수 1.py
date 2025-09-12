import sys
input = sys.stdin.readline
def fib(n):
    cnt = [0] * (n+1)
    cnt[1] = 1
    cnt[2] = 1
    for i in range(3,n+1):
        cnt[i] = cnt[i-1] + cnt[i-2]
    return cnt[n]
a = int(input())
print(fib(a),a-2)