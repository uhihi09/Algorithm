a,b,c = map(int,input().split(" : "))
a1,b1,c1 = map(int,input().split(" : "))
cnt1 = a*3600+b*60+c
cnt2 = a1*3600+b1*60+c1
if cnt2 - cnt1 == 0:
    print(0)
elif cnt2 - cnt1 < 0:
    cnt1 -= 86400
    ans = (cnt1 - cnt2)*-1
    print(ans)
else:
    print(cnt2-cnt1)