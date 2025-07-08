def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
a = int(input())
b = list(map(int,input().split()))
c = int(input())
cnt = []
for i in b:
    if gcd(i,c) ==1:
        cnt.append(i)
print(sum(cnt)/len(cnt))