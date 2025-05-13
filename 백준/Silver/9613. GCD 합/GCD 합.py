def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)
a = int(input())
for i in range(a):
    b = list(map(int,input().split()))
    ans = []
    for ii in range(1,len(b)):
        for iii in range(ii+1,len(b)):
            ans.append(gcd(b[ii],b[iii]))
    print(sum(ans))