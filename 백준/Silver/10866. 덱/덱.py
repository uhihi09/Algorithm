import sys
input = sys.stdin.readline
def push_front(a):
    cnt.insert(0,a)
def push_back(a):
    cnt.append(a)
def pop_front():
    if len(cnt) == 0:
        print(-1)
    else:
        print(cnt[0])
        cnt.pop(0)
def pop_back():
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
cnt = []
for i in range(a):
    b = list(input().split())
    if len(b) == 2:
        b[1] = int(b[1])
    if b[0] == "push_front":
        push_front(b[1])
    elif b[0] == "push_back":
        push_back(b[1])
    elif b[0] == "pop_front":
        pop_front()
    elif b[0] == "pop_back":
        pop_back()
    elif b[0] == "size":
        size()
    elif b[0] == "empty":
        empty()
    elif b[0] == "front":
        front()
    elif b[0] == "back":
        back()