a,b = map(int,input().split())
ans = []
ans1 = []
cnt = 0
for i in range(a):
    ans.append(list(input()))
cnt1 = input()
for i in range(a):
    ans1.append(list(input()))
for i in range(a):
    for j in range(b):
        if ans[i][j] == ans1[i][j]:
            cnt += 1
print(cnt)