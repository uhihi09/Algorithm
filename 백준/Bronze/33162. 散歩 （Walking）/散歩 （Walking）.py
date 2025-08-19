a = int(input())
cnt = True
ans = 0
for i in range(a):
    if cnt:
        ans += 3
        cnt = False
    else:
        ans -= 2
        cnt = True
print(ans)