a,b = map(int,input().split(":"))
c,d = map(int,input().split(":"))
if a > c:
    print("NO")
elif c > a:
    print("YES")
else:
    if b > d:
        print("NO")
    else:
        print("YES")