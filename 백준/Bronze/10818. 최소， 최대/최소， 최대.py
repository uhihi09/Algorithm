a = int(input())
c = []
b = list(map(int, input().split()))
for i in range(1, a+1):
    c.append(b)
print(min(b),max(b))