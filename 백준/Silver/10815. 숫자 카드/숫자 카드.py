import sys
input = sys.stdin.readline
a = int(input())
b = list(map(int,input().split()))
c = int(input())
d = list(map(int,input().split()))
b = set(b)
cnt = [0 for i in range(c)]
for i in range(len(d)):
    if d[i] in b:
        cnt[i] = 1
print(*cnt)