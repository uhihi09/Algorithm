a = int(input())
b,c,d = map(int,input().split())
if a <= b+c+d or a <= 240:
    print("high speed rail")
else:
    print("flight")