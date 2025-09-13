import sys
input = sys.stdin.readline
def love(a):
    cnt = [0] * 10001
    cnt[1] = 1
    cnt[2] = 1
    for i in range(3, a+1):
        cnt[i] = cnt[i-1] + cnt[i-2]
    return cnt[a]
while True:
    a = int(input())
    if a == -1:
        break
    print(f"Hour {a}: {love(a)} cow(s) affected")