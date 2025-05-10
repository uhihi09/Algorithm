a = int(input())
ans = 0
for i in range(a):
    b = list(input())
    cnt = 0
    for ii in b:
        if ii == "O":
            cnt += 1
        else:
            cnt = 0
        ans += cnt
    print(ans)
    ans = 0