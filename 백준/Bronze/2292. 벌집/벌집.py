a = int(input())
if a == 1:
    print(1)
else:
    cnt1 = 1
    cnt = 1
    plus = 6
    while cnt1 < a:
        cnt1 += plus
        cnt += 1
        plus += 6
    print(cnt)