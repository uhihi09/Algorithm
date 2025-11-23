def find(a, b, c):
    if b == "+":
        return a + c
    else:
        return a - c
a = int(input())
for i in range(int(input())):
    b = input()
    c = int(input())
    a = find(a, b, c)

print(a)
