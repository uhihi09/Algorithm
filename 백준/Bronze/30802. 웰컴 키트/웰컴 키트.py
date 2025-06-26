a = int(input())
b = list(map(int, input().split()))
c,d = map(int, input().split())
cnt = 0
for i in b:
    if i != 0:
        if i%c ==0:
            cnt += i//c
        else:
            cnt += (i//c)+1
print(cnt)
print(a//d,a%d)