a = int(input())
b = 0
c = a
for i in range(a-1,-1,-1):
    b += 1
    for ii in range(i):
        print(" ",end="")
    for ii in range(b):
        print("*",end="")
    print()
for i in range(1,a):
    c -= 1
    for ii in range(i):
        print(" ",end="")
    for ii in range(c):
        print("*",end="")
    print()