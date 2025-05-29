a = int(input())
ans = []
for i in range(666,10000000):
    if '666' in str(i):
        ans.append(i)
print(ans[a-1])