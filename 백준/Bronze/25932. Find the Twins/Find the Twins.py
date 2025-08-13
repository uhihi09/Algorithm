a = int(input())
for i in range(a):
    b = list(map(int, input().split()))
    if 18 in b and 17 in b:
        print(*b)
        print("both")
    elif 18 in b:
        print(*b)
        print("mack")
    elif 17 in b:
        print(*b)
        print("zack")
    else:
        print(*b)
        print("none")
    print()