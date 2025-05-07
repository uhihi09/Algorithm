a,b = map(int, input().split())
s = a+b
p = (a**2+b**2)**(0.5)
if int(p) == p:
    print(int(s-p))
else:
    print(s-p)