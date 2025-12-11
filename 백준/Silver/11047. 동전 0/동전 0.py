a,b = map(int,input().split())
cnt = [int(input()) for i in range(a)]
cnt.sort(reverse=True)
ans = 0
for i in cnt:
    if b // i != 0:
        ans += b//i
        b %= i
print(ans)