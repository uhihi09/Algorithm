a = int(input())
b = int(input())
c = int(input())
d = a*b*c
e = []
f = [0,1,2,3,4,5,6,7,8,9]
g = str(d)
n0 = 0
n1 = 0
n2 = 0
n3 = 0
n4 = 0
n5 = 0
n6 = 0
n7 = 0
n8 = 0
n9 = 0
for i in range(len(g)):
    e.append(g[i])
for i in e:
    if i == "0":
        n0 += 1
    elif i == "1":
        n1 += 1
    elif i == "2":
        n2 += 1
    elif i == "3":
        n3 += 1
    elif i == "4":
        n4 += 1
    elif i == "5":
        n5 += 1
    elif i == "6":
        n6 += 1
    elif i == "7":
        n7 += 1
    elif i == "8":
        n8 += 1
    elif i == "9":
        n9 += 1
print(n0)
print(n1)
print(n2)
print(n3)
print(n4)
print(n5)
print(n6)
print(n7)
print(n8)
print(n9)