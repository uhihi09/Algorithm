a1,b1,c1 = map(int,input().split())
a2,b2,c2 = map(int,input().split())
a1 -= a2
b1 -= b2
c1 -= c2
cnt = 0
if a1 < 0:
    cnt += a1*-1
if b1 < 0:
    cnt += b1*-1
if c1 < 0:
    cnt += c1*-1
print(cnt)