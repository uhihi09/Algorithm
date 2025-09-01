a,b = map(int,input().split())
cnt = []
for i in range(1,a+1):
    if a % i == 0:
        cnt.append(i)
try:
    print(cnt[b-1])
except:
    print(0)