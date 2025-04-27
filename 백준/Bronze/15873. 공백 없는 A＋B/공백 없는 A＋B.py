a = input()
if len(a) == 2:
    print(int(a[0])+int(a[1]))
elif len(a) == 3:
    if int(a[0:2]) > 10:
        print(int(a[0])+int(a[1:3]))
    else:
        print(int(a[0:2])+int(a[2:4]))
elif len(a) == 4:
    print(int(a[0:2])+int(a[2:4]))