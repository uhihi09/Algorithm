import sys
input = sys.stdin.readline
udyr = 10007
def fac(a):
    ans = 1
    for i in range(2,a+1):
        ans *= i
    return ans
def love(a,b):
    return fac(a) // fac(b) // fac(a-b)
a,b = map(int,input().split())
print(love(a,b)%udyr)