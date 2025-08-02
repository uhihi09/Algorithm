a,b = map(int,input().split())
cnt = []
for i in range(a):
    cnt.append(int(input()))
for i in range(len(cnt)):
    print(cnt[i]*(b//sum(cnt)))