a,b = map(int,input().split())
if a %2 != 0 and b % 2 != 0:
    print(min(a,b))
else:
    print(0)