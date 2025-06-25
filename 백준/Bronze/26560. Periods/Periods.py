a = int(input())
for i in range(a):
    b = list(input())
    if b[-1] != ".":
        b.append(".")
        print(*b,sep="")
    else:
        print(*b,sep="")