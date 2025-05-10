b = []
ans = []
for i in range(10):
    a = int(input())
    a %= 42
    b.append(a)
for i in b:
    if i not in ans:
        ans.append(i)
print(len(ans))