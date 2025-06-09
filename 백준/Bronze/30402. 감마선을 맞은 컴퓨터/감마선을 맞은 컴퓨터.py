def love():
    ans = []
    for i in range(15):
        ans.append(list(input().split()))
    for i in ans:
        for ii in i:
            if "w" == ii :
                print("chunbae")
                return
            elif "b" == ii:
                print("nabi")
                return
            elif "g" == ii:
                print("yeongcheol")
                return
love()