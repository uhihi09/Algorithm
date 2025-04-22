h,m,s = map(int, input().split())
sp = int(input())
sp += s
while sp >= 60 or h >= 60 or h >= 24:
    if sp >= 60:
        sp -= 60
        m += 1
    if m >= 60:
        m -= 60
        h += 1
    if h >= 24:
        h -= 24
print(h,m,sp)