a = int(input())
b = a-1
c = a-1
for i in range(1,a+1):
    print("*"*i,end="")
    print(" "*b*2,end="")
    print("*"*i)
    b-=1
b+=2
for i in range(c,0,-1):
    print("*"*i,end="")
    print(" "*b*2,end="")
    print("*"*i)
    b+=1