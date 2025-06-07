a = int(input())
b = a*2-1+2
for i in range(a):
    b -= 2
    for ii in range(i):
        print(" ",end="")
    for ii in range(b):
        print("*",end="")
    print()