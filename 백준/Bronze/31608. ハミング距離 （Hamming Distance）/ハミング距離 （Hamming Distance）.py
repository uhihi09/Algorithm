a = int(input())
b = input()
c = input()
cnt = 0
for i in range(a):
    if b[i] != c[i]:
        cnt += 1
print(cnt)