a = int(input())
for i in range(a):
    A1,P1 = map(int,input().split())
    A2,P2 = map(int,input().split())
    cnt = A2**2*3.141592
    if A1 / P1 > cnt/P2:
        print("Slice of pizza")
    else:
        print("Whole pizza")