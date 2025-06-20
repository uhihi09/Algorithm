a,b = map(int,input().split())
c,d = map(int,input().split())
cnt1 = a/b
cnt2 = (3.1415926535*c**2)/d
if cnt1 >= cnt2:
    print("Slice of pizza")
else:
    print("Whole pizza")