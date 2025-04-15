a = int(input())
for i in range(a,0,-1):
    for ii in range(a-i):
        print(" ",end="")
    for iii in range(i*2-1):
        print("*",end="")
    print()
for iv in range(1,a):
    for v in range(a-iv-1):
        print(" ",end="")
    for vi in range(iv*2+1):
        print("*",end="")
    print()