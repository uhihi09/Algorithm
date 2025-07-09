cnt = []
row = []
for i in range(9):
    a = list(map(int, input().split()))
    cnt.append(a)
for i in range(len(cnt)):
    row.append(max(cnt[i]))
print(max(row))
for i in range(len(cnt)):
    for ii in range(len(cnt[i])):
        if cnt[i][ii] == max(row):
            print(i+1,ii+1)