import sys
input = sys.stdin.readline
n,k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
ans1 = sum(a)
ans2 = sum(b)
for i in range(k):
    if ans1 >= ans2:
        ans1 -= a.pop()
    elif ans1 < ans2:
        ans2 -= b.pop()
print(max(ans1,ans2))