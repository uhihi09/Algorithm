def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
while True:
    a,b = map(int,input().split())
    if a == 0 and b == 0:
        break
    elif a == b:
        print(1)
    elif a%b == 0 or b%a == 0:
        print(max(a,b)//min(a,b))
    elif gcd(a,b) != 1:
        print(a*b//gcd(a,b))
    else:
        print(a*b)