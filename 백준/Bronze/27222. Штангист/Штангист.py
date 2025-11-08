a = int(input())
b = list(map(int, input().split()))
ans = 0

for i in range(a):
    L, R = map(int, input().split())
    if b[i]:
        ans += max(R - L, 0)

print(ans)
