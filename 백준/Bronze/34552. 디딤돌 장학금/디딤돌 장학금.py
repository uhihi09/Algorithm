a = list(map(int,input().split()))
b = int(input())
cnt = 0
for i in range(b):
    c, d, e = map(float, input().split())
    c = int(c)
    e = int(e)
    if d >= 2.0 and e >= 17:
        cnt += a[c]
print(cnt)