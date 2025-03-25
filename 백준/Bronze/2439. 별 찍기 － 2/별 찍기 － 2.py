a = int(input())
b = 0
c = a
for i in range(1,a+1):
    b += 1
    c -= 1
    print(" "*c,"*"*i,sep="")