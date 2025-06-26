while True:
    a = list(map(int, input().split()))
    if a[0] == 0 and a[1] == 0 and a[2] == 0:
        break
    cnt = 0
    for i in range(3):
        if a[i] != max(a) and a[i] != min(a):
            cnt = a[i]
    if max(a)**2 == (min(a)**2)+(cnt**2):
        print("right")
    else:
        print("wrong")