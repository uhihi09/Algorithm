a,b = map(int,input().split())
c = int(input())
for i in range(c):
    d = int(input())
    if d < 1000:
        print(d,d*a)
    else:
        print(d,(d-1000)*b+1000*a)