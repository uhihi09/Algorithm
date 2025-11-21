a = int(input())
if a >= 1000000:
    print(int(a*(20/100)),int(a*(80/100)))
elif 500000 <= a < 1000000:
    print(int(a*(15/100)),int(a*(85/100)))
elif 100000 <= a < 500000:
    print(int(a*(10/100)),int(a*(90/100)))
else:
    print(int(a*(5/100)),int(a*(95/100)))