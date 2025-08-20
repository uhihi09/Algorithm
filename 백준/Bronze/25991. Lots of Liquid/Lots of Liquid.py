a = int(input())
b = list(map(float, input().split()))
cnt = 0
for i in range(len(b)):
    cnt += b[i]**3
print(cnt**(1/3))