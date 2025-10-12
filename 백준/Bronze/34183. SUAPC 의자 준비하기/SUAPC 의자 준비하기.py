a,b,c,d = map(int,input().split())
if a*3 <= b:
    print(0)
else:
    print(((a*3)-b)*c+d)