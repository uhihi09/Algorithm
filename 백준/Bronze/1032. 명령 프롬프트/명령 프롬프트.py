a = int(input())
cnt = list(input())
for i in range(a-1):
    b = input()
    for ii in range(len(cnt)):
        if cnt[ii] != b[ii]:
            cnt[ii] = "?"
print("".join(cnt))