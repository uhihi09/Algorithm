a,b = map(int,input().split())
c = list(map(int,input().split()))
cnt = []
for i in range(a-1):
    cnt.append(c[i] * b + c[i+1]*b)
print(min(cnt))