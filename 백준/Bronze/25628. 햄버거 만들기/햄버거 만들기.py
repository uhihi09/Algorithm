a,b = map(int, input().split())
a = a//2
if a < 1:
    print(0)
elif a > b:
    print(b)
elif b> a:
    print(a)
else:
    print(a)