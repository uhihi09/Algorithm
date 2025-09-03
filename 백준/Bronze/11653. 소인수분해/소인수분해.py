a = int(input())
b = 2
while a != 1:
    if a % b != 0:
        b += 1
    else:
        a //= b
        print(b)