n,k,a,b = map(int,input().split())
cnt1 = (abs(k-1) + (n-1)) * b
cnt2 = (n-1) * a
print(cnt1,cnt2)