a,b = map(int,input().split())
c,d = map(int,input().split())
cnt = c+d
if c+d <= b:
    cnt1 = c
else:
    cnt1 = -1
for i in range(a-1):
    c,d = map(int,input().split())
    if c+d <= b:
        if c+d > cnt:
            cnt = c+d
            cnt1 = c
print(cnt1)