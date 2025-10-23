a,b = map(int,input().split())
saved = 0
now = 0
for i in range(a):
    c = input()
    if c == "save":
        saved = now
    elif c == "load":
        now = saved
    elif c == "shoot":
        now -= 1
    elif c == "ammo":
        now += b
    print(now)