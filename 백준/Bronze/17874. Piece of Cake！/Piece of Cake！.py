a,b,c = map(int,input().split())
cnt1 = max(a-b,b)
cnt2 = max(a-c,c)
print(cnt1*cnt2*4)