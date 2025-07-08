def gcd(a, b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
a = int(input())
for i in range(a):
    b = int(input())
    c = int(input())
    print(gcd(b,c))