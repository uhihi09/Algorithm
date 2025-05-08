a = int(input())
b,c = map(int,input().split())
b //= 2
c = b+c
if a >= c:
    print(c)
else:
    print(a)