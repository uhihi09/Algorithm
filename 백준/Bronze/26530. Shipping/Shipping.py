a = int(input())
for i in range(a):
    e = int(input())
    ans = 0
    for ii in range(e):
        b,c,d = input().split()
        c = int(c)
        d = float(d)
        ans += c*d
    print(f"${ans:.2f}")