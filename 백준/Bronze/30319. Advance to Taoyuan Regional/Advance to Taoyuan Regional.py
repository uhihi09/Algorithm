a,b,c = map(int,input().split("-"))
if b == 9:
    if c > 16:
        print("TOO LATE")
    else:
        print("GOOD")
elif b > 9:
    print("TOO LATE")
else:
    print("GOOD")