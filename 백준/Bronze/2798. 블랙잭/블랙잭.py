a,b = map(int,input().split())
c = list(map(int,input().split()))
cnt = 0
for i in range(a):
    for ii in range(a):
        for iii in range(a):
            if i != ii and i != iii and ii != iii:
                if b >= c[i] + c[ii] + c[iii] >= cnt:
                    cnt = c[i] + c[ii] + c[iii]
print(cnt)