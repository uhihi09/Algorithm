a = int(input())
cnt = []
ans = []
for i in range(a):
    b,c = map(int,input().split())
    cnt.append((b,c))
for i in range(len(cnt)):
    b,c = cnt[i][0],cnt[i][1]
    ans2 = 1
    for ii in range(len(cnt)):
        if b < cnt[ii][0] and c < cnt[ii][1]:
            ans2 += 1
    ans.append(ans2)
print(*ans)