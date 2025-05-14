def gcd(a,b):
    cnt = 0
    while a != b:
        if a>b:
            a = a -b
        else:
            b = b- a
        cnt += 1
    return cnt
a,b = map(int,input().split())
print(gcd(a,b))