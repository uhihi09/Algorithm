ans = 0
for i in range(10):
    a = int(input())
    if a == 1:
        ans += 90
    elif a == 2:
        ans += 180
    elif a== 3:
        ans -=90
if ans%360 == 0:
    print("N")
elif ans%360 == 90:
    print("E")
elif ans%360 == 180:
    print("S")
elif ans%360 == 270:
    print("W")