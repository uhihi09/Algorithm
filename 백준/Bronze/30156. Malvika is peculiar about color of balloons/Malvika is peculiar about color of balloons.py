a = int(input())
for i in range(a):
    b = list(input())
    if b.count("b") >= b.count("a"):
        print(b.count("a"))
    elif b.count("a") > b.count("b"):
        print(b.count("b"))