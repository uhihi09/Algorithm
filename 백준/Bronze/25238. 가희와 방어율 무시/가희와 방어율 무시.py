a,b = map(int, input().split())
c =  int(a-(a*b*0.01))
if a < 100:
    print(1)
elif c >= 100:
    print(0)
else:
    print(1)