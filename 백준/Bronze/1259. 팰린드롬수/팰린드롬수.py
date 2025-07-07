while True:
    a = input()
    if a == "0":
        break
    cnt = 0
    for i in range(len(a)):
        if a[i] == a[len(a)-i-1]:
            cnt += 1
    if cnt == len(a):
        print("yes")
    else:
        print("no")