a,b = map(int,input().split())
cnt = []
ans = []
c = 0
for i in range(1,a+1):
    cnt.append(i)
for i in range(len(cnt)):
    c = (c + b -1) % len(cnt)
    ans.append(cnt[c])
    cnt.pop(c)
print("<",end="")
for i in range(len(ans)-1):
    print(ans[i],end="")
    print(",",end=" ")
print(ans[-1],end="")
print(">")