a = int(input())
for i in range(a):
    b,c = map(float,input().split())
    ans = b-c
    if ans < 0:
        ans *= -1
        print(f"{ans:.1f}")
    else:
        print(f"{ans:.1f}")