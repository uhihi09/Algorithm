while True:
    a = int(input())
    if a == 0:
        break
    b = list(map(int,input().split()))
    if a <= 3:
        print(sum(b))
    else:
        cnt = []
        for i in range(2,len(b)):
            cnt.append(b[i-2] + b[i-1] + b[i])
        print(max(cnt))