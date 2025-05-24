a = int(input())
b,c,d = map(int,input().split())
if b > a:
    b = a
if c > a:
    c = a
if d > a:
    d = a
print(b+c+d)