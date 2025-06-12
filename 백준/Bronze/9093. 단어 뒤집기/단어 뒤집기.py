a = int(input())
for i in range(a):
    b = list(input().split())
    for ii in b:
        ii = list(ii)
        ii.reverse()
        for iii in ii:
            print(iii,end="")
        print(" ",end="")