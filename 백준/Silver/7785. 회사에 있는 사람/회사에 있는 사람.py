import sys
input = sys.stdin.readline
a = int(input())
cnt = set()
for i in range(a):
    b,c = input().strip().split()
    if c == "enter":
        cnt.add(b)
    else:
        cnt.remove(b)
cnt = list(cnt)
cnt.sort(reverse=True)
for i in cnt:
    print(i)