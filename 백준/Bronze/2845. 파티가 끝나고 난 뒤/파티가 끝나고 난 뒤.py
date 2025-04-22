a,b = map(int, input().split())
a *= b
c = list(map(int,input().split()))
for i in c:
    print(i-a,end=" ")