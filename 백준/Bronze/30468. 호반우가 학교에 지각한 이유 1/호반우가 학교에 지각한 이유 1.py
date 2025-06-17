a = list(map(int,input().split()))
ans = (a[-1]*4)-sum(a[:4])
if ans <= 0:
    print(0)
else:
    print(ans)