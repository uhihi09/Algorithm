a = int(input())
cnt1 = []
cnt2 = []
ans = 0
for i in range(a):
    cnt1.append(input())
for i in range(a):
    cnt2.append(input())
for i in range(len(cnt1)):
    if cnt1[i] == cnt2[i]:
        ans += 1
print(ans)