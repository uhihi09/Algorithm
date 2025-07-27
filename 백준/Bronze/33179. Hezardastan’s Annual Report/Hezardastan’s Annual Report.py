a = int(input())
b = list(map(int, input().split()))
cnt = 0
for i in b:
    if i%2 == 0:
        cnt += i//2
    else:
        cnt += i//2+1
print(cnt)