a = int(input())
cnt = []
cnt1 = []
for i in range(1,a+1):
    cnt.append(i)
for i in range(len(cnt)-1):
    cnt1.append(cnt[0])
    cnt.pop(0)
    cnt.append(cnt[0])
    cnt.pop(0)
cnt1.append(cnt[0])
print(*cnt1)