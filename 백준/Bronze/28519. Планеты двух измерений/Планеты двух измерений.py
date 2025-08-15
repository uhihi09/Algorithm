a,b = map(int,input().split())
ans = 0
if max(a,b) - min(a,b) < 1:
    ans = a+b
elif max(a,b) - min(a,b) == 1:
    ans = a+b
else:
    ans = min(a,b) + min(a,b) +1
print(ans)