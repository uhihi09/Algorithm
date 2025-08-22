import sys
input = sys.stdin.readline
a = int(input())
cnt = []
ans = 1
for i in range(a):
    cnt.append(int(input()))
cnt1 = cnt[-1]
for i in range(len(cnt)-1,-1,-1):
    if cnt[i] > cnt1:
        ans += 1
        cnt1 = cnt[i]
print(ans)