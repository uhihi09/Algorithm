a = int(input())
b = 0
for i in range(a):
    c = int(input())
    if c%2 != 0:
        b += 1
print(b)