def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

a1,a2 = map(int, input().split())
b1,b2 = map(int, input().split())
c1 = a1*b2 + b1*a2
c2 = a2*b2
print(c1//gcd(c1,c2),c2//gcd(c1,c2))