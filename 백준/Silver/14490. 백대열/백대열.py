def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)
    
a,b = map(int, input().split(":"))
print(f"{a//gcd(a,b)}:{b//gcd(a,b)}")