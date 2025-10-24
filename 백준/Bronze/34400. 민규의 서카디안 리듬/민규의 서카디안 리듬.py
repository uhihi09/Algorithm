a = int(input())
for i in range(a):
    b = int(input())
    if b % 25 < 17:
        print("ONLINE")
    else:
        print("OFFLINE")