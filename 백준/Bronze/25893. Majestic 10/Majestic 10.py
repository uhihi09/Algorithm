a = int(input())
for i in range(a):
    b = list(map(int, input().split()))
    print(*b)
    cnt = 0
    for ii in b:
        if ii >= 10:
            cnt += 1
    if cnt == 0:
        print("zilch")
    elif cnt == 1:
        print("double")
    elif cnt == 2:
        print("double-double")
    elif cnt == 3:
        print("triple-double")
    print()