a,b,c =map(int,input().split())
cnt1 = 0
cnt2 = a
ans = 0
while cnt1 < cnt2:
    cnt1+=c
    cnt2+=b
    ans+=1
print(ans)