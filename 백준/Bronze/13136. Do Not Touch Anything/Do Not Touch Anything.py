a,b,c = map(int,input().split())
ans1 = 0
ans2 = 0
if a%c != 0:
    ans1 += a//c+1
elif a%c == 0:
    ans1 += a//c
if b%c != 0:
    ans2 += b//c+1
elif b%c == 0:
    ans2 += b//c
print(ans1 * ans2)