def gcd(a,b):
    if b ==0:
        return a
    else:
        return gcd(b,a%b)
a = int(input())
for i in range(a):
    b,c = map(int, input().split())
    print(b*c//(gcd(b,c)))