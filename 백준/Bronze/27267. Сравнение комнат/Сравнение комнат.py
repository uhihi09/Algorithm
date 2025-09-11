a,b,c,d =map(int,input().split())
if a*b > c*d:
    print("M")
elif c*d > a*b :
    print("P")
else:
    print("E")