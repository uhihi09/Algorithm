a,b = map(int,input().split())
c,d = map(int,input().split())
if (a+b)%4 == 0:
    ans1 = 4
else:
    ans1 = (a+b)%4
if (c+d+ans1)%4 == 0:
    ans2 = 4
else:
    ans2 = (c+d+ans1)%4
print((ans2+2)%4+1)