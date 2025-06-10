a = int(input())
for i in range(a):
    b,c,d = map(float, input().split())
    sum = b*c*d
    print(f'${sum:.2f}')