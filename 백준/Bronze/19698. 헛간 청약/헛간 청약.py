a,b,c,d = map(int, input().split())
ans = (b//d)*(c//d)
if ans > a:
    print(a)
else:
    print(ans)