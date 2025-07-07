a = int(input())
x = int(input())
b = int(input())
y = int(input())
t = int(input())
if t > 45:
    print(((t-30)*x)*21+a)
    print(((t-45)*y)*21+b)
elif 30 < t <= 45:
    print(((t-30)*x)*21+a)
    print(b)
else:
    print(a)
    print(b)