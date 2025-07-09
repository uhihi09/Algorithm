def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
def lcm(a,b):
        return a*b//gcd(a,b)
a = int(input())
cnt = []
ans = 0
for i in range(a):
    cnt.append(int(input()))
ans = cnt[0]
for i in range(1, len(cnt)):
    ans = lcm(ans, cnt[i])
print(ans)