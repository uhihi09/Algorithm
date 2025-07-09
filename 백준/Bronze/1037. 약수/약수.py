a = int(input())
b = list(map(int, input().split()))
if len(b) == 1:
    print(b[0]**2)
elif len(b) == 2:
    print(b[0]*b[1])
else:
    print(max(b)*min(b))