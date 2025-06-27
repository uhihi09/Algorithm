a = int(input())
cnt = 0
for i in range(a):
    b,c = map(int,input().split())
    if b == 136:
        cnt += 1000
    elif b == 142:
        cnt += 5000
    elif b == 148:
        cnt += 10000
    elif b == 154:
        cnt += 50000
print(cnt)