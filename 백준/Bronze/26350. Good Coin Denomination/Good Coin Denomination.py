a = int(input())
for i in range(a):
    b = list(map(int, input().split()))
    b = b[1:]
    cnt = True
    for ii in range(1,len(b)):
        if b[ii] >= b[ii-1]*2:
            continue
        else:
            cnt = False
            break
    print("Denominations:", *b)
    if cnt:
        print(f"Good coin denominations!\n")
    else:
        print("Bad coin denominations!\n")