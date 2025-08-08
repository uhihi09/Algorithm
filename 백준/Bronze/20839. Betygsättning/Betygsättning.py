a,b,c = map(int,input().split())
d,e,f = map(int,input().split())
if a <= d and b <= e and c <= f:
    print("A")
elif a/2 <= d and b <= e and c <= f:
    print("B")
elif b <= e and c <= f:
    print("C")
elif b/2 <= e and c <= f:
    print("D")
elif c <= f:
    print("E")