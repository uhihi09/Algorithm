a = int(input())
x,y = map(int,input().split())
ans = y
ans2 = (x,y)
for i in range(a-1):
    x,y = map(int,input().split())
    if y < ans:
        ans = y
        ans2 = (x,y)
print(ans2[0],ans2[1])