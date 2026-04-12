import sys
input = sys.stdin.readline
a,b = map(int,input().split())
c = set(map(int,input().strip().split()))
d = set(map(int,input().strip().split()))
cnt1 = len(c - d)
cnt2 = len(d - c)
print(cnt1+cnt2)