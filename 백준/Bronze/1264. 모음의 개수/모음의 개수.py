while True:
    a = input()
    b = 0
    if a == "#":
        break
    for i in range(len(a)):
        if "a" in a[i] or "e" in a[i] or "i" in a[i] or "o" in a[i] or "u" in a[i] or "A" in a[i] or "E" in a[i] or "I" in a[i] or "O" in a[i] or "U" in a[i]:
            b += 1
    print(b)