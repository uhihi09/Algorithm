a = int(input())
cnt = 1
while cnt <= 1000000:
    cnt2 = cnt
    for i in range(len(str(cnt))):
        cnt2 += int(str(cnt)[i])
    if cnt2 == a:
        print(cnt)
        break
    cnt += 1
else:
    print(0)