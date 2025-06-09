ans = []
for i in range(5):
    a = int(input())
    ans.append(a)
for i in ans:
    if ans.count(i) >= 2 and i in ans:
        ans.remove(i)
        ans.remove(i)
print(ans[0])