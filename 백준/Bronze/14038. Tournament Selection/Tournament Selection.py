cnt = []
ans = 0
for i in range(6):
    cnt.append(input())
for i in cnt:
    if i == "W":
        ans += 1
if ans == 0:
    print(-1)
elif ans >= 5:
    print(1)
elif ans >= 3:
    print(2)
else:
    print(3)