import sys
input = sys.stdin.readline
def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)
def lcm(a,b):
    return (a*b)//gcd(a,b)
a = int(input())
for i in range(a):
    e = int(input())
    cnt = list(map(int,input().split()))
    wow = cnt[0]
    for ii in range(1,len(cnt)):
        wow = lcm(cnt[ii],wow)
    if wow <= 1000000000:
        print(wow)
    else:
        print("More than a billion.")