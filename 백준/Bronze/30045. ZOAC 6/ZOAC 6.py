a = int(input())
cnt = 0
for i in range(a):
    b = list(input())
    cnt1 = b[-1]
    for ii in range(len(b) - 1):
        if b[ii] == "O" and b[ii+1] == "I":
            cnt += 1
            break
        elif b[ii] == "0" and b[ii+1] == "1":
            cnt += 1
            break
print(cnt)