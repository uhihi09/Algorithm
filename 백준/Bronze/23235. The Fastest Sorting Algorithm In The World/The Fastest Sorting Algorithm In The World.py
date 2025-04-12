b = 0
while True:
    a = list(map(int, input().split()))
    b += 1
    if a[0] == 0:
        break
    else:
        print(f"Case {b}: Sorting... done!")