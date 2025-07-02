a,b = map(int,input().split())
c,d = map(int,input().split())
cnt1 = a*3+b
cnt2 = c*3+d
if cnt1 > cnt2:
    print(1,cnt1-cnt2)
elif cnt2 > cnt1:
    print(2,cnt2-cnt1)
else:
    print("NO SCORE")