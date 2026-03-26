import sys
input = sys.stdin.readline
n,m = map(int,input().split())
cnt1 = set()
cnt2 = set()
for i in range(n):
    cnt1.add(input().strip())
for i in range(m):
    cnt2.add(input().strip())
ans = list(cnt1 & cnt2)
ans.sort()
print(len(ans))
for i in ans:
    print(i)