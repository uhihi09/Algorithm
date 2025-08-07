a = int(input())
for i in range(1,a+1):
    b,c,d = map(int,input().split())
    ans = 0
    for ii in range(b):
        e,f = map(int,input().split())
        if c*d >= e:
            ans += f
    print(f"Data Set {i}:")
    print(ans)
    print()