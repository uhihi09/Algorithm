import sys
input = sys.stdin.readline
def one(a):
    cnt.append(a)
def two(a):
    if len(cnt) == 0:
        print(-1)
    else:
        print(cnt[-1])
        cnt.pop()
def three(a):
    print(len(cnt))
def four(a):
    if len(cnt) == 0:
        print(1)
    else:
        print(0)
def five(a):
    if len(cnt) == 0:
        print(-1)
    else:
        print(cnt[-1])
a = int(input())
cnt = []
for i in range(a):
    a = list(map(int, input().split()))
    if a[0] == 1:
        one(a[1])
    elif a[0] == 2:
        two(a[0])
    elif a[0] == 3:
        three(a[0])
    elif a[0] == 4:
        four(a[0])
    elif a[0] == 5:
        five(a[0])