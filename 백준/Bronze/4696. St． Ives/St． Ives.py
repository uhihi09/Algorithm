while True:
    a = float(input())
    if a == 0:
        break
    else:
        print(f"{float(a**4 + a ** 3 + a ** 2 + a ** 1 + a ** 0):.2f}")