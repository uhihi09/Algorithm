a = input()
cnt = 0
ans = ""
while True:
    ans += a[cnt]
    if cnt == len(a)-1:
        break
    cnt1 = ord(a[cnt]) - ord('A') + 1
    cnt += cnt1
print(ans)