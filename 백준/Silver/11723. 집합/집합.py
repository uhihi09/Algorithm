import sys
input = sys.stdin.readline
S = set()
A = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
a = int(input())
for i in range(a):
    b = list(input().split())
    if len(b) == 2:
        x = int(b[1])
    if b[0] == "add":
        if x not in S:
            S.add(x)
    elif b[0] == "remove":
        if x in S:
            S.discard(x)
    elif b[0] == "check":
        if x in S:
            print(1)
        else:
            print(0)
    elif b[0] == "toggle":
        if x in S:
            S.discard(x)
        else:
            S.add(x)
    elif b[0] == "all":
        S = A.copy()
    elif b[0] == "empty":
        S.clear()