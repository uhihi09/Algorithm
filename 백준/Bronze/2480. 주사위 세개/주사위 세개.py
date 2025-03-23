a,b,c = map(int, input().split())
if a == b == c:
    print(10000+(a)*1000)
elif a == b or b == c or a == c:
    if a==b:
        print(1000+(a)*100)
    elif c==b:
        print(1000+(b)*100)
    elif a==c:
        print(1000+(c)*100)
elif a>b>c or b>c>a or c>a>b or a>c>b or b>a>c or c>b>a:
    if a>b>c or a>c>b:
        print(a*100)
    elif b>c>a or b>a>c:
        print(b*100)
    elif c>a>b or c>b>a:
        print(c*100)