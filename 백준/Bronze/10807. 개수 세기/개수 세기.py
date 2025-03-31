a = int(input())
b = list(map(int, input().split()))
c = int(input())
t = 0
for i in range(0,a):
    if b[i] == c:
        t += 1
print(t)