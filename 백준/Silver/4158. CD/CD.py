import sys
input = sys.stdin.readline
while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    cnt1 = set()
    cnt2 = set()
    for i in range(a):
        cnt1.add(int(input().strip()))
    for i in range(b):
        cnt2.add(int(input().strip()))
    print(len(cnt1 & cnt2))