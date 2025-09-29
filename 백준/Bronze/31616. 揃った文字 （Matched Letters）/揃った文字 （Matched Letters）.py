a = int(input())
b = input()
ans = True
if len(b) == 1:
    pass
else:
    for i in range(1,len(b)):
        if b[i-1] == b[i]:
            ans = True
        else:
            ans = False
            break
if ans:
    print("Yes")
else:
    print("No")