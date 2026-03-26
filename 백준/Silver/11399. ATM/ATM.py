import sys
input = sys.stdin.readline
a = int(input())
n = list(map(int,input().strip().split()))
n.sort()
cnt1 = 0
cnt2 = 0
for i in range(len(n)):
    cnt2 += n[i]
    cnt1 += cnt2
print(cnt1)