a = int(input())
cnt1 = 0
cnt2 = 0
d = []
for i in range(a):
    b,c = map(int,input().split())
    cnt1 += b
    cnt2 += c
    if c >= b:
        d.append(c)
    elif cnt2 < cnt1:
        d.append(-1)
print(min(d))