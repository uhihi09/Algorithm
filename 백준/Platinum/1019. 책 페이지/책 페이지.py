import sys
input = sys.stdin.readline
N = int(input().strip())
cnt = [0] * 10
p = 1
while p <= N:
    cnt[0] -= p
    for d in range(10):
        high = N//(p*10)
        cur = (N//p)%10
        low = N%p
        if cur > d:
            cnt[d] += p*high+p
        elif cur == d:
            cnt[d] += p*high+low+1
        elif cur < d:
            cnt[d] += p*high
    p *= 10
print(*cnt)