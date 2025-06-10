import sys
input = sys.stdin.readline
a,b,c = map(int,input().split())
if (b-a)/c == int((b-a)/c):
    print(int((b-a)/c))
else:
    print(int((b-a)/c)+1)