a = int(input())
b = list(map(int,input().split()))
c = set(b)
c = list(c)
c.sort()
for i in c:
    print(i)