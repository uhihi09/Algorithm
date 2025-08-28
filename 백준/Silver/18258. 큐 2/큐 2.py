import sys
input = sys.stdin.readline
from collections import deque
def push(a):
    cnt.append(a)
def pop():
    if len(cnt) == 0:
        print(-1)
    else:
        print(cnt.popleft())
def size():
    print(len(cnt))
def empty():
    if len(cnt) == 0:
        print(1)
    else:
        print(0)
def front():
    if len(cnt) == 0:
        print(-1)
    else:
        print(cnt[0])
def back():
    if len(cnt) == 0:
        print(-1)
    else:
        print(cnt[-1])
a = int(input())
cnt = deque()
for i in range(a):
    b = list(input().split())
    if len(b) == 2:
        b[1] = int(b[1])
    if b[0] == "push":
        push(b[1])
    elif b[0] == "pop":
        pop()
    elif b[0] == "size":
        size()
    elif b[0] == "empty":
        empty()
    elif b[0] == "front":
        front()
    elif b[0] == "back":
        back()