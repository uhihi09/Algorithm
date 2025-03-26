a = []
for i in range(1,10):
    b = int(input())
    a.append(b)
c = max(a)
print(c)
print(a.index(c)+1)