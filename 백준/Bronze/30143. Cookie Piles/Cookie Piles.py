a = int(input())
for i in range(a):
    b,c,d = map(int,input().split())
    cnt = c
    ans = 0
    for ii in range(b):
        ans += cnt
        cnt += d
    print(ans)