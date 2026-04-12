import collections
import sys
input = sys.stdin.readline
n = int(input())
deque = collections.deque()
for i in range(n):
    a = list(map(int,input().strip().split()))
    if a[0] == 1:
        deque.appendleft(a[1])
    elif a[0] == 2:
        deque.append(a[1])
    elif a[0] == 3:
        if len(deque) == 0:
            print(-1)
        else:
            print(deque.popleft())
    elif a[0] == 4:
        if len(deque) == 0:
            print(-1)
        else:
            print(deque.pop())
    elif a[0] == 5:
        print(len(deque))
    elif a[0] == 6:
        if len(deque) == 0:
            print(1)
        else:
            print(0)
    elif a[0] == 7:
        if len(deque) == 0:
            print(-1)
        else:
            var = deque.popleft()
            print(var)
            deque.appendleft(var)
    elif a[0] == 8:
        if len(deque) == 0:
            print(-1)
        else:
            var = deque.pop()
            print(var)
            deque.append(var)