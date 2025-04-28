import sys
def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)
a,b = map(int, sys.stdin.readline().split())
print(10**gcd(a,b)//9)