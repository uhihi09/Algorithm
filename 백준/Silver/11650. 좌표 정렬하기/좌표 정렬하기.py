import sys
input = sys.stdin.readline
a = int(input())
cnt = []
for i in range(a):
    b,c = map(int,input().split())
    cnt.append([b,c])
cnt.sort()
for i in range(a):
    print(cnt[i][0],cnt[i][1])