import sys
input = sys.stdin.readline
a = int(input())
cnt = {}
for i in range(a):
    var = input().strip()
    cnt[var] = cnt.get(var, 0) + 1
for i in range(a-1):
    cnt[input().strip()] -= 1
for i in cnt.keys():
    if cnt[i] != 0:
        print(i)