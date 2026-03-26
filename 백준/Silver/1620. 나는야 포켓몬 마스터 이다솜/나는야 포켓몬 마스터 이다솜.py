import sys
input = sys.stdin.readline
a,b = map(int,input().split())
cnt1 = {}
cnt2 = {}
for i in range(1,a+1):
    var2 = input().strip()
    cnt1[var2] = i
    cnt2[i] = var2
for i in range(b):
    var = input().strip()
    if var.isdigit():
        print(cnt2[int(var)])
    else:
        print(cnt1[var])