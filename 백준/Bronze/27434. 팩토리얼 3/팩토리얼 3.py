a = int(input())
b = 1
if a !=0:
    for i in range(1,a+1):
        b *= i
    print(b)
elif a ==0:
    print(1)