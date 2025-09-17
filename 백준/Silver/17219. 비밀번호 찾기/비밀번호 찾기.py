import sys
input = sys.stdin.readline
a,b = map(int,input().split())
cnt1 = {}
for i in range(a):
    c,d = input().split()
    cnt1[c] = d
for i in range(b):
    a = input().strip()
    print(cnt1[a])