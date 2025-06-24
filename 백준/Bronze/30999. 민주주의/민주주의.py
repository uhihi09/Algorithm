a,b =  map(int,input().split())
cnt = b//2+1
cnt1 = 0
for i in range(a):
    c = list(input())
    if c.count("O") >= cnt:
        cnt1 += 1
print(cnt1)