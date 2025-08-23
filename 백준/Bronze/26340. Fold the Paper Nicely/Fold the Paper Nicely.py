a = int(input())
for i in range(a):
    b,c,d = map(int,input().split())
    print(f"Data set: {b} {c} {d}")
    for i in range(d):
        if b >= c:
            b //= 2
        else:
            c //= 2
    print(max(b,c),min(b,c))
    print()