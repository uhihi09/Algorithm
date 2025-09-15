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
n = int(input())
print(pac(n)//(pac(4)*pac(n-4)))