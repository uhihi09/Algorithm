def love(a):
    ans = []
    for i in range(1,a+1):
        if a%i == 0:
            ans.append(i)
    if len(ans) == 2:
        return 1
    else:
        return 0
a = int(input())
b = list(map(int,input().split()))
cnt = 0
for i in b:
    cnt += love(i)
print(cnt)