a = int(input())
b = -1
for i in range(a,0,-1):
    b += 2
    for ii in range(i-1,0,-1):
        print(" ",end="")
    for ii in range(b):
        print("*",end="")
    print()