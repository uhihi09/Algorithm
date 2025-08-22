a = int(input())
for i in range(a):
    a = list(input().split())
    a = a[::-1]
    print(f"Case #{i+1}: {' '.join(map(str, a))}")