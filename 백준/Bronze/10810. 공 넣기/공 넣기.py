a,b = map(int,input().split())
ans = [0 for i in range(a)]
for i in range(b):
    c,d,e = map(int,input().split())
    for ii in range(c-1,d):
        ans[ii] = e
for i in ans:
    print(i,end=" ")