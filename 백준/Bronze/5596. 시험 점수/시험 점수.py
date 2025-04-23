a,b,c,d = map(int, input().split())
e,f,g,h = map(int, input().split())
cnt1 = a+b+c+d
cnt2 = e+f+g+h
if cnt1 >= cnt2:
    print(cnt1)
else:
    print(cnt2)