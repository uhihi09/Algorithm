def answer(a,b):
    cnt = [True] * (b+1)
    if a == 1:
        cnt[0] = False
    ans = []
    for i in range(2,b+1):
        if cnt[i] and i >= a:
            ans.append(i)
        for j in range(i*2,b+1,i):
            cnt[j] = False
    return ans
a,b = map(int,input().split())
ans = answer(a,b)
for i in ans:
    print(i)