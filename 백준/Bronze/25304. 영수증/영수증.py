t = int(input())
n = int(input())
c = 0
y = 0
for i in range(1,n+1):
    a,b = map(int,input().split())
    c = a*b
    y += c
if t == y:
    print("Yes")
else:
    print("No")