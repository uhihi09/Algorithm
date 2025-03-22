a,b = map(int, input().split())
if (b-45)>0:
    print(a,b-45)
elif (b-45)<0 and a ==0:
    b +=60
    print(23,b-45)
elif (b-45)<0:
    b +=60
    print(a-1,b-45)
else:
    print(a,0)