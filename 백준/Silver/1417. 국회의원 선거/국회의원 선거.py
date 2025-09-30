a = int(input())
cnt = []
cnt1 = 0
for i in range(a):
    cnt.append(int(input()))
try:
    while cnt[0] <= max(cnt[1:]):
        cnt[cnt[1:].index(max(cnt[1:]))+1] -= 1
        cnt[0] += 1
        cnt1 += 1
except:
    cnt1 = 0
print(cnt1)