a = int(input())
b = list(map(int,input().split()))
cnt = 10000000000
cnt1 = 0
for i in b:
    if i < cnt:
        cnt = i
    elif cnt < i:
        cnt1 = max(i-cnt,cnt1)
print(cnt1)