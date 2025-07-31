def love(a):
    c = 1
    cnt = ''
    while len(a) != len(cnt):
        cnt += str(c)
        if a[:len(cnt)] != cnt:
            return -1
        c += 1
    c -= 1
    if a == cnt:
        return c
    else:
        return -1
b = input()
print(love(b))