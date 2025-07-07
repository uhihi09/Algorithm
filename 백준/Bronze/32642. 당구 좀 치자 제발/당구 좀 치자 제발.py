b = int(input())
a = list(map(int, input().split()))
cnt = 0
ans = 0
for i in a:
    if i == 1:
        cnt += 1
    else:
        cnt -= 1
    ans += cnt
print(ans)