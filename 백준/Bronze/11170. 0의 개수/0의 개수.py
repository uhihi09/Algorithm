a = int(input())
for i in range(a):
    b,c = map(int,input().split())
    cnt = 0
    for ii in range(b,c+1):
        ii = str(ii)
        ii = list(ii)
        cnt += ii.count("0")
    print(cnt)