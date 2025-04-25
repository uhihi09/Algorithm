l = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())
cnt1 = 0
cnt3 = 0
if a%c == 0:
    cnt1 = a//c
else:
    cnt1 = a//c+1
if b%d == 0:
    cnt3 = b//d
else:
    cnt3 = b//d+1
if cnt1 > cnt3:
    print(l-cnt1)
else:
    print(l-cnt3)