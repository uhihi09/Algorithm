a,b = map(int,input().split())
c,d = map(int,input().split())
if c+d <= b:
    cnt = c
else:
    cnt = -1
for i in range(a-1):
    c,d = map(int,input().split())
    if c+d <= b:
        if cnt < c:
            cnt = c
print(cnt)