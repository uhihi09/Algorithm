a = int(input())
for i in range(a):
    b = int(input())
    c = int(input())
    cnt = [[0] * c for ii in range(b+1)]
    for ii in range(1,c+1):
        cnt[0][ii-1] = ii
    for ii in range(1,b+1):
        for iii in range(c):
            cnt[ii][iii] = sum(cnt[ii-1][:iii+1])
    print(cnt[b][c-1])