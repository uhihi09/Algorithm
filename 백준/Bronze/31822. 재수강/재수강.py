a = list(input())
b = int(input())
cnt = a[:5]
ans = 0
for i in range(b):
    c = list(input())
    if c[:5] == cnt:
        ans += 1
print(ans)