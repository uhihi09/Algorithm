a = int(input())
b = a
c = 0
for i in range(1,a*2,2):
    b -= 1
    for ii in range(b):
        print(" ", end="")
    for ii in range(i):
        print("*", end="")
    print()
for i in range(a*2-3,0,-2):
    c += 1
    for ii in range(c):
        print(" ", end="")
    for ii in range(i):
        print("*", end="")
    print()