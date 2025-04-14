a = int(input())
b = 1
for i in range(1,a+1):
    b *= i
if a == 0:
    print(1)
else:
    print(b)