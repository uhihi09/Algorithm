while True:
    a,b = map(int, input().split())
    if a > b:
        print("Yes")
    elif b >= a and (b != 0 or a != 0):
        print("No")
    elif a or b == 0:
        break