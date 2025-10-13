high = 11
low = 0
while True:
    a = int(input())
    if a == 0:
        break
    b = input()
    if b == "too high":
        high = min(a,high)
    elif b == "too low":
        low = max(a,low)
    elif b == "right on":
        if low < a < high:
            print("Stan may be honest")
            high = 11
            low = 0
        else:
            print("Stan is dishonest")
            high = 11
            low = 0