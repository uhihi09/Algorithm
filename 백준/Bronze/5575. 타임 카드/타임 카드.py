for i in range(3):
    a = list(map(int,input().split()))
    go = a[0]*3600+a[1]*60+a[2]
    leave = a[3]*3600+a[4]*60+a[5]
    ans = leave-go
    h = ans//3600
    m = (ans%3600)//60
    s = (ans%3600)%60
    print(h,m,s)