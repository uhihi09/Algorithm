a,b,c = map(int,input().split())
cnt = a*1440+b*60+c
cnt1 = 11*1440+11*60+11
if cnt1 > cnt:
    print(-1)
else:
    print(cnt-cnt1)