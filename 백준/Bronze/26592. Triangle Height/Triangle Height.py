a = int(input())
for i in range(a):
    b,c = map(float,input().split())
    print(f"The height of the triangle is {(b*2)/c:.2f} units")