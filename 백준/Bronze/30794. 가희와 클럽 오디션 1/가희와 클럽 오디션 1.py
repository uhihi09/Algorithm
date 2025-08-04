x, s = input().split()
x = int(x)

if s == "miss":
    print(x * 0)
elif s == "bad":
    print(x * 200)
elif s == "cool":
    print(x * 400)
elif s == "great":
    print(x * 600)
elif s == "perfect":
    print(x * 1000)