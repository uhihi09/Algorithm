cnt = {"j":2, "o":1, "i":2}
b = int(input())
a = list(input())
cnt1 = 0
for i in a:
    cnt1 += cnt[i]
print(cnt1)