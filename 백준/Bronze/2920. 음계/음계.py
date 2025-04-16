a1,a2,a3,a4,a5,a6,a7,a8 = map(int, input().split())
if a1 == 1 and a2 == 2 and a3 == 3 and a4 == 4 and a5 == 5 and a6 == 6 and a7 == 7 and a8 == 8:
    print("ascending")
elif a1 == 8 and a2 == 7 and a3 == 6 and a4 == 5 and a5 == 4 and a6 == 3 and a7 == 2 and a8 == 1:
    print("descending")
else:
    print("mixed")