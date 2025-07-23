def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
a = int(input())
b = list(map(int,input().split()))
cnt = b[0]
b = b[1:]
for i in range(len(b)):
    print(f"{cnt//gcd(cnt,b[i])}/{b[i]//gcd(cnt,b[i])}")