a = int(input())
b = list(map(int, input().split()))
c = list(map(int, input().split()))
cnt = 0
for i in range(a):
    if b[i] <= c[i]:
        cnt += 1
print(cnt)