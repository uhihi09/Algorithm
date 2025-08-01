a = int(input())
b,c = map(int,input().split())
cnt1 = b
cnt2 = c
ans = "yes"
for i in range(a-1):
    c,d = map(int,input().split())
    if c >= cnt1 and d >= cnt2:
        ans = "yes"
        cnt1 = c
        cnt2 = d
    else:
        ans = "no"
        break
print(ans)