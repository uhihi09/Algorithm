a,b,c = map(int,input().split())
cnt = a
cnt1 = 0
for i in range(c):
    cnt = (cnt%b)*10
print(cnt//b)