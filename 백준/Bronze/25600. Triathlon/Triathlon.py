a = int(input())
cnt = []
for i in range(a):
    b,c,d = map(int,input().split())
    if b == (c+d):
        cnt.append((b*(c+d))*2)
    else:
        cnt.append(b*(c+d))
print(max(cnt))