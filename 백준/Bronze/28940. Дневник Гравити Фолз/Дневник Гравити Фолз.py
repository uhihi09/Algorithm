import math
w,h = map(int,input().split())
a,b,c = map(int,input().split())
if w >= b and h >= c:
    cnt = (w//b)*(h//c)
    print(math.ceil(a/cnt))
else:
    print(-1)