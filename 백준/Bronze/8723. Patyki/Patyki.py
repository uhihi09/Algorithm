a = list(map(int,input().split()))
b = a.copy()
b.remove(max(a))
b.remove(min(a))
if a[0] == a[1] == a[2]:
    print(2)
elif max(a)**2 == min(a)**2+b[0]**2:
    print(1)
else:
    print(0)