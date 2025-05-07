a,b = map(int, input().split())
c = int(input())
c *= 2
if a+b >= c:
    print(a+b-c)
else:
    print(a+b)