a = int(input())
cnt = a
ans = 0
while True:
    if cnt <= 0:
        break
    if cnt // 5 > 0:
        if cnt % 5 == 0:
            cnt -= 5
            ans += 1
        elif cnt % 3 == 0:
            cnt -= 3
            ans += 1
        elif cnt - 5 == cnt % 3 == 0:
            ans += 1
        else:
            cnt -= 5
            ans += 1
    elif cnt // 3 > 0:
        cnt -= 3
        ans += 1
    else:
        ans = -1
        break
print(ans)