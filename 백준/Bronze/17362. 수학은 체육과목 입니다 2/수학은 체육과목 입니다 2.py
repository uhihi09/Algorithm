a = int(input())
if a%8 == 1:
    print(1)
elif a%8 == 0 or a%8 == 2:
    print(2)
elif a%8 == 3 or a%8 == 7:
    print(3)
elif a%8 == 4 or a%8 == 6:
    print(4)
else:
    print(5)