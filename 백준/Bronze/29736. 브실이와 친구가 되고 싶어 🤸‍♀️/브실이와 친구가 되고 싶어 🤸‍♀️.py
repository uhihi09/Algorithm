a,b = map(int,input().split())
k,x = map(int,input().split())
ans = 0
for i in range(a,b+1):
    if k>= i:
        if k-i <= x:
            ans += 1
    elif k<i:
        if i-k <= x:
            ans += 1
if ans == 0 :
    print("IMPOSSIBLE")
else:
    print(ans)