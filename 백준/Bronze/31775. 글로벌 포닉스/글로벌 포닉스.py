a = input()
b = input()
c = input()
cnt = ["l","k","p"]
if a[0] in cnt:
    cnt.remove(a[0])
    if b[0] in cnt:
        cnt.remove(b[0])
        if c[0] in cnt:
            print("GLOBAL")
        else:
            print("PONIX")
    else:
        print("PONIX")
else:
    print("PONIX")