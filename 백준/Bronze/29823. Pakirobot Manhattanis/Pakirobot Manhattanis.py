a = int(input())
b = list(input())
x,y = 0,0
for i in b:
    if i == "N":
        y += 1
    elif i == "S":
        y -= 1
    elif i == "W":
        x += 1
    elif i == "E":
        x -= 1
print(abs(x)+abs(y))