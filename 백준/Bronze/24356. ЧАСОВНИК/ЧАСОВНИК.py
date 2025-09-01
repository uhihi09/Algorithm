a1,a2,b1,b2 = map(int,input().split())
ans = (b1-a1)*60 + (b2-a2)
if ans < 0:
    ans += 1440
print(ans,ans//30)