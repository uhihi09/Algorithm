a,b = map(int,input().split())
c,d = map(int,input().split())
ans1 = b-a
ans2 = d-c
while ans1 != ans2:
    if ans1 < ans2:
        ans1 += b
    else:
        ans2 += d
print(ans1)