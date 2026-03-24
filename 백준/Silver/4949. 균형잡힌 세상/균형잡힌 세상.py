import collections
while True:
    a = list(input())
    if (len(a) == 1) and (a[0] == "."):
        break
    if len(a) == 1:
        print("no")
    cnt = collections.deque()
    for i in range(len(a)):
        if a[i] == "(" or a[i] == "[":
            cnt.append(a[i])
        elif a[i] == ")":
            if len(cnt) == 0:
                print("no")
                break
            if cnt.pop() != "(":
                print("no")
                break
        elif a[i] == "]":
            if len(cnt) == 0:
                print("no")
                break
            if cnt.pop() != "[":
                print("no")
                break
    else:
        if len(cnt) != 0:
            print("no")
        else:
            print("yes")