a = int(input())
for i in range(a):
    b = int(input())
    cnt = {}
    for ii in range(b):
        b,c = input().split()
        c = int(c)
        cnt[c] =  b
    ans = sorted(cnt, reverse=True)
    print(cnt[ans[0]])