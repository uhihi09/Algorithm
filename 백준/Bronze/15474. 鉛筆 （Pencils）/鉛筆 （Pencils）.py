a,b,c,d,e = map(int,input().split())
if a%b != 0:
    cnt1 = a//b+1
else:
    cnt1 = a//b
if a%d !=0:
    cnt2 = a//d+1
else:
    cnt2 = a//d
if cnt1*c <= cnt2*e:
    print(cnt1*c)
else:
    print(cnt2*e)