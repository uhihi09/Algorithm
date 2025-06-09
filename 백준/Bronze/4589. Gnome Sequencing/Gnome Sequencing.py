a = int(input())
print("Gnomes:")
for i in range(a):
    b = list(map(int,input().split()))
    c = b.copy()
    c.sort()
    d = b.copy()
    d.sort(reverse=True)
    if b == c or b == d:
        print("Ordered")
    else:
        print("Unordered")