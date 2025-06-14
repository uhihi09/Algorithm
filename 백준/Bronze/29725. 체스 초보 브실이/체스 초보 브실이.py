def love(a):
    if a == "K" or a == "k":
        return 0
    elif a == "P" or a == "p":
        return 1
    elif a == "N" or a == "n" or a == "B" or a == "b":
        return 3
    elif a == "R" or a == "r":
        return 5
    else :
        return 9
cnt = []
ans1 = 0
ans2 = 0
for i in range(8):
    a = list(input())
    for ii in a:
        if ii != ".":
            cnt.append(ii)
for i in cnt:
    if i.isupper():
        ans1 += love(i)
    elif i.islower():
        ans2 += love(i)
print(ans1-ans2)