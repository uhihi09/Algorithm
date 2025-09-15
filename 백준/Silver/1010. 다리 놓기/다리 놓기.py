import sys
input = sys.stdin.readline
def pac(a):
    if a <= 1:
        return 1
    else:
        cnt = 1
        for i in range(1,a+1):
            cnt *= i
        return cnt
a = int(input())
for i in range(a):
    r,n = map(int,input().split())
    print(pac(n)//(pac(r)*pac(n-r)))