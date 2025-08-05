a,b = map(int,input().split())
ans = True
for i in range(a):
    c = list(input().split())
    if c.count('A') != 1:
        ans = False
if ans:
    print('Yes')
else:
    print('No')