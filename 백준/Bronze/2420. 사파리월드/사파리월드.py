a,b = map(int, input().split())
if a-b < 0:
    print((a-b)*-1)
elif a-b > 0:
    print(a-b)