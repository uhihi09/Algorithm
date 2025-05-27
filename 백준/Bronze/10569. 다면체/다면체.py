# -a+b+2=c
a = int(input())
ans = 0
for i in range(a):
    b,c = map(int,input().split())
    ans = -b+c+2
    print(ans)