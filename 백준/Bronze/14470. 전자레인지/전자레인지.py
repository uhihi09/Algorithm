a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
ans = a
s = 0
if a < 0:
    while True:
        if ans == b:
            print(s+e)
            break
        elif ans < 0:
            ans += 1
            s += c
        elif ans == 0:
            s += d
            ans += 1
        elif ans > 0:
            s += e
            ans += 1
else:
    while True:
        if ans == b:
            print(s)
            break
        elif ans < 0:
            ans += 1
            s += c
        elif ans == 0:
            s += d
            ans += 1
        elif ans > 0:
            s += e
            ans += 1