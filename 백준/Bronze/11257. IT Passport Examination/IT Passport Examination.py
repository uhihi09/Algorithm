for i in range(int(input())):
    a,b,c,d = map(int,input().split())
    if b >= 11 and c >= 8 and d >= 12 and d + b + c >= 55:
        cnt = "PASS"
    else:
        cnt = "FAIL"
    print(a,b+c+d,cnt)