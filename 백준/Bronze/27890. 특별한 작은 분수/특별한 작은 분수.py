a,b = map(int,input().split())
ans = a
for i in range(b):
    if ans % 2 ==0:
        ans //= 2
        ans ^= 6
    else:
        ans *= 2
        ans ^= 6
print(ans)