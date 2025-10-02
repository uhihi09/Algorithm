a = int(input())
cnt = 0
for i in range(a):
    b = list(input())
    cnt1 = []
    ans = True
    if len(b) == 1:
        ans = True
    else:
        cnt1.append(b[0])
        for ii in range(1,len(b)):
            if b[ii] not in cnt1:
                cnt1.append(b[ii])
            elif b[ii] in cnt1:
                if b[ii-1] == b[ii]:
                    continue
                else:
                    ans = False
                    break
            else:
                ans = False
                break
    if ans:
        cnt += 1
print(cnt)