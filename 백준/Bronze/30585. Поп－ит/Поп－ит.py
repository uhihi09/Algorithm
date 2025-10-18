a,b = map(int,input().split())
cnt1 = 0
cnt2 = 0
for i in range(a):
    c = list(input())
    for ii in c:
        if ii == "0":
            cnt1 += 1
        elif ii == "1":
            cnt2 += 1
print(min(cnt1,cnt2))