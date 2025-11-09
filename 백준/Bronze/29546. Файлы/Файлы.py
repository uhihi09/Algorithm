a = int(input())
b = [input() for _ in range(a)]
c = int(input())
d = []
for _ in range(c):
    e, f = map(int, input().split())
    for i in range(e - 1, f):
        d.append(b[i])
print("\n".join(d))