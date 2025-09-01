a = int(input())
ans = 0
cnt = a
while True:
    one = cnt // 10
    two = cnt % 10
    cnt = two * 10 + (one + two) % 10
    ans += 1
    if cnt == a:
        break
print(ans)