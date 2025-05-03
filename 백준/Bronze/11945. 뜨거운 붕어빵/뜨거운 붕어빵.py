a,b = map(int, input().split())
for i in range(a):
    c = list(input())
    c.reverse()
    print(*c,sep="")