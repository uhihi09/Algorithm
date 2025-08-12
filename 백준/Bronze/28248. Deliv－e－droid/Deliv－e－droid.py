a = int(input())
b = int(input())
ans = 0
ans += a*50
ans += -10*b
if a > b:
    ans += 500
print(ans)