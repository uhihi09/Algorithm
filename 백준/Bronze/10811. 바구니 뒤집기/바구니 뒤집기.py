a,b = map(int,input().split())
ans = [i for i in range(1,a+1)]
for i in range(b):
    c,d = map(int,input().split())
    ans[c-1:d] = ans[c-1:d][::-1]
for i in ans:
    print(i,end=" ")