a = input()
ans = f"{a[0]}"
for i in range(1,len(a)):
    if a[i] != a[i-1]:
        ans += a[i]
print(ans)