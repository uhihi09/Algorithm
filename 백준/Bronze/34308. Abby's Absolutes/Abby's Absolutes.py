a,b = map(int,input().split())
c = list(map(int,input().split()))
if a % 2 != 0:
    sanghan = a//2 + 1
else:
    sanghan = a//2
for i in c:
    if i <= sanghan:
        print(1,end=" ")
    else:
        print(a,end =" ")