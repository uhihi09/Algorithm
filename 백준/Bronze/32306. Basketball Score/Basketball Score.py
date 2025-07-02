a,b,c = map(int,input().split())
d,e,f = map(int,input().split())
cnt1 = a+b*2+c*3
cnt2 = d+e*2+f*3
if cnt1 > cnt2:
    print(1)
elif cnt2 > cnt1:
    print(2)
else:
    print(0)