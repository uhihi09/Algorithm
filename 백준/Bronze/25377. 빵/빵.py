a = int(input())
cnt = 0
ans = 0
ans1 = True
ans2 = 0
for i in range(a):
    b,c = map(int, input().split())
    cnt += b
    ans += c
    if ans < cnt:
        ans1 = False
    elif ans >= cnt:
        if c-b >= 0:
            ans2 += (c - b)
        else:
            ans2 += b-c
if ans1 == False:
    print(-1)
else:
    print(ans2)