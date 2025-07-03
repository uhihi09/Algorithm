while True:
    try:
        for i in range(7):
            a = list(input())
            for ii in range(len(a)):
                if a[ii] == "i":
                    a[ii] = "e"
                elif a[ii] == "e":
                    a[ii] = "i"
                elif a[ii] == "I":
                    a[ii] = "E"
                elif a[ii] == "E":
                    a[ii] = "I"
            for ii in a:
                print(ii,end="")
            print()
    except EOFError:
        break