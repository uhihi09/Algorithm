a = input()
b = int(a)
if "7" not in a :
    if b%7 == 0:
        print(1)
    elif b%7 != 0:
        print(0)
elif "7" in a:
    if b%7 == 0:
        print(3)
    else:
        print(2)