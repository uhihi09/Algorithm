n,m = map(int,input().split())
cnt1, cnt2 = {}, {}
ans = 0
for i in range(n):
    var = input()
    cnt1[var] = 0
for i in range(m):
    var = input()
    if var in cnt2.keys():
        cnt2[var] += 1
    else:
        cnt2[var] = 1
for i in cnt2.keys():
    if i in cnt1.keys():
        ans += cnt2[i]
print(ans)