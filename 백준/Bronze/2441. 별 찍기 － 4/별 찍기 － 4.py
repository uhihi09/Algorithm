a = int(input())
for i in range(a):
    for ii in range(i):
        print(" ",end="")
    for iii in range(a-i):
        print("*",end="")
    print()