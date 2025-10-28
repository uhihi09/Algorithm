def find(a):
    while len(a) != 0:
        if a[0] != a[-1]:
            return 0
        else:
            if len(a) == 1:
                a.pop(0)
            else:
                a.pop(0)
                a.pop(-1)
    return 1
a = list(input())
print(find(a))