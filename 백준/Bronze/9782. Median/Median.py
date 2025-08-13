cnt = 1
while True:
    a = list(map(int, input().split()))
    ans = 0
    if a[0] == 0:
        break
    for i in range(1,len(a)):
        if a[0]%2 == 0:
            ans = (a[a[0]//2] + a[a[0]//2+1])/2
        else:
            ans = float(a[a[0]//2+1])
    print(f"Case {cnt}: {ans}")
    cnt += 1