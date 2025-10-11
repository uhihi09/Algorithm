a,b = map(int,input().split())
c = list(map(int,input().split()))
ans = 0
for i in c:
    ans += i // b
print(ans)