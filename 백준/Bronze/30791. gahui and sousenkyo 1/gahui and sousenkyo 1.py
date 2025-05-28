b = list(map(int,input().split()))
ans = -1
for i in b:
    if b[0]-1000 <= i:
        ans += 1
print(ans)