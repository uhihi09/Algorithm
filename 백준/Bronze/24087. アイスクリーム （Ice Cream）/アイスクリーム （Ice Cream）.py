a = int(input())
b = int(input())
c = int(input())
cnt = 0
if a > b:
    cnt = a-b
    if cnt % c != 0:
        print(250+(cnt//c+1)*100)
    else:
        print(250+(cnt//c)*100)
else:
    print(250)