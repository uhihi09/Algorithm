import sys
input = sys.stdin.readline
def love(a):
    cnt = [0] * 10001
    cnt[1] = 1
    cnt[2] = 2
    for i in range(3, a+1):
        cnt[i] = cnt[i-1] + cnt[i-2]
    return cnt[a]
a = int(input())
print(love(a))