a,b,c = map(int, input().split())
if a-b > a-c:
    print("Bus")
elif a-c > a-b:
    print("Subway")
else:
    print("Anything")