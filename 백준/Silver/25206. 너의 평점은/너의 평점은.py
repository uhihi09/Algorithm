def love(a):
    p = {
        "A+":4.5, "A0":4.0, "B+":3.5, "B0":3.0, "C+":2.5, "C0":2.0, "D+":1.5, "D0":1.0, "F":0.0, "P":523
    }
    if a == "P":
        return False
    else:
        return p[a]

cnt = 0
cnt1 = 0
for i in range(20):
    a,b,c = input().split()
    b = float(b)
    if c != "P":
        c = love(c)
        cnt += b * c
        cnt1 += b
if cnt1 == 0:
    print("0.000000")
else:
    print(f"{cnt/cnt1:.6f}")