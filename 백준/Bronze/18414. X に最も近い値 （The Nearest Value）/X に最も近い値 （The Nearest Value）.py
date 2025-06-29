a,b,c = map(int,input().split())
cnt = b
for i in range(b,c+1):
    if a > i:
        if a-i <= a-cnt:
            cnt = i
            cnt1 = a-i
    elif a < i:
        if i-a <= cnt-a:
            cnt = i
            cnt1 = i-a
    elif a == i:
        cnt = i
        break
print(cnt)