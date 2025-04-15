a,b = map(int, input().split())
l = [i for i in range(1, 46) for _ in range(i)]
d = 0
for ii in range(a-1,b):
    d = d + l[ii]
print(d)