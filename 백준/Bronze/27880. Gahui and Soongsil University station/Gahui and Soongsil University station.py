ans = 0
for _ in range(4):
    a,b = input().split()
    b = int(b)
    if a == "Es":
        ans += b*21
    else:
        ans += b*17
print(ans)