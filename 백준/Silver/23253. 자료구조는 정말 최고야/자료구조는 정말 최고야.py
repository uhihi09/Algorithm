import sys
input = sys.stdin.readline
n,m = map(int,input().split())
cnt = []
cnt1 = 1
ans = []
for i in range(m):
    a = int(input())
    cnt.append(list(map(int,input().split())))
for i in range(len(cnt)):
    for ii in range(len(cnt[i])-1):
        if cnt[i][ii] > cnt[i][ii+1]:
            ans.append(True)
        else:
            ans.append(False)
            break
if False not in ans:
    print("Yes")
else:
    print("No")