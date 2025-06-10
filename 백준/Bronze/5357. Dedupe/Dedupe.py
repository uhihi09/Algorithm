a = int(input())
for i in range(a):
    b = list(input())
    ans = b[0]
    print(ans,end="")
    for ii in range(1,len(b)):
        if b[ii] != ans:
            ans = b[ii]
            print(ans,end="")
    print()