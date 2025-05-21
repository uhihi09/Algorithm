a = int(input())
cnt = 1
for i in range(1,a+1):
    cnt *= i
cnt = str(cnt)
ans = 0
for i in range(len(cnt)-1,-1,-1):
    if cnt[i] == "0":
        ans += 1
    else:
        break
print(ans)