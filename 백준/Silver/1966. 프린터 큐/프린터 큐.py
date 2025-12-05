a = int(input())
for i in range(a):
    b,c = map(int,input().split())
    d = list(map(int,input().split()))
    cnt = 0
    while True:
        if d[0] == max(d):
            d.pop(0)
            cnt += 1
            if c == 0:
                print(cnt)
                break
            else:
                c -= 1
        else:
            d.append(d.pop(0))
            if c == 0:
                c = len(d) - 1
            else:
                c -= 1