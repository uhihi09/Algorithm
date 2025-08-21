import sys
input = sys.stdin.readline
def push(n):
    cnt.append(n)
def pop():
    if len(cnt) == 0:
        print(-1)
    else:
        print(cnt[-1])
        cnt.pop(-1)
def size():
    print(len(cnt))
def empty():
    if len(cnt) == 0:
        print(1)
    else:
        print(0)
def top():
    if len(cnt) == 0:
        print(-1)
    else:
        print(cnt[-1])
a = int(input())
cnt = []
for i in range(a):
    a = list(input().split())
    if len(a) == 2:
        b = int(a[1])
    if a[0] == "push":
        push(b)
    elif a[0] == "pop":
        pop()
    elif a[0] == "size":
        size()
    elif a[0] == "empty":
        empty()
    elif a[0] == "top":
        top()