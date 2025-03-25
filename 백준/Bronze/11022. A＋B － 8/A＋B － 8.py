a = int(input())
d = 0
for i in range(1, a+1):
    d += 1
    b,c = map(int, input().split())
    print(f"Case #{d}: {b} + {c} = {b+c}")