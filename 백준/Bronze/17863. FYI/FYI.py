a = list(map(int,input()))
cnt = 0
for i in range(3):
    if a[i] == 5:
        cnt += 1
if cnt >= 3:
    print("YES")
else:
    print("NO")