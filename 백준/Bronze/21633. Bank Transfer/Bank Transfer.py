a = int(input())
ans = 25 + (a*(1/100))
if ans < 100:
    ans = 100.00
elif ans > 2000:
    ans = 2000.00
print(f"{ans:.2f}")