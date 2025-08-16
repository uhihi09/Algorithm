a = int(input())
for i in range(a):
    b,c = map(int,input().split())
    if (b <= 1 and c <=2) or (b <= 2 and c <= 1):
        print("Yes")
    else:
        print("No")