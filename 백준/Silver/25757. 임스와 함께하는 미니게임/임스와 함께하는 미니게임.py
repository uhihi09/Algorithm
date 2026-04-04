import sys
input = sys.stdin.readline
a,b = input().split()
a = int(a)
cnt = set()
for i in range(a):
    cnt.add(input().strip())
if b == "Y":
    print(len(cnt))
elif b == "F":
    print(len(cnt)//2)
elif b == "O":
    print(len(cnt)//3)