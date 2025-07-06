a = int(input())
cnt = []
ans = 0
for i in range(a):
    cnt.append(int(input()))
b = int(input())
for i in range(b):
    c = int(input())
    ans += cnt[c-1]
print(ans)