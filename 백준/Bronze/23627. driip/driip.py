a = list(input())
while True:
    try:
        if a[-5] == "d" and a[-4] == "r" and a[-3] == "i" and a[-2] == "i" and a[-1] == "p":
            print("cute")
            break
        else:
            print("not cute")
            break
    except:
        print("not cute")
        break