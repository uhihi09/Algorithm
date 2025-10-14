a,b = map(int,input().split())
cnt = 0
for i in range(a):
    b = list(input())
    if "+" in b:
        cnt += 1
print(cnt)