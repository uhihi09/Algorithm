a = int(input())
d = []
for i in range(a):
    b,c = map(int,input().split())
    if c >= b:
        d.append(c)
if len(d) > 0:
    print(min(d))
else:
    print(-1)