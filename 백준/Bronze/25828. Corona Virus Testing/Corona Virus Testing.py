a,b,c = map(int,input().split())
ans1 = a*b
ans2 = a+b*c
if ans1 < ans2:
    print(1)
elif ans2 < ans1:
    print(2)
else:
    print(0)