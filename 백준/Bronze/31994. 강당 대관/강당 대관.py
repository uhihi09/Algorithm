ans = {}
cnt = []
for i in range(7):
    a,b = input().split()
    b = int(b)
    ans[b] = a
    cnt.append(b)
print(ans[max(cnt)])