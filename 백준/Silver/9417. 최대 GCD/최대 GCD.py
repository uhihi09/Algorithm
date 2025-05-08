def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
a = int(input())
for i in range(a):
    a = list(map(int,input().split()))
    ans = []
    for ii in range(len(a)):
        for iii in range(ii + 1, len(a)):
            ans.append(gcd(a[ii],a[iii]))
    print(max(ans))