a1,b1 = map(int,input().split())
b2,a2 = map(int,input().split())
if a1 + a2 > b1+ b2:
    print("Persepolis")
elif b1 + b2 > a1 + a2:
    print("Esteghlal")
else:
    if b1 > a2:
        print("Esteghlal")
    elif a2 > b1:
        print("Persepolis")
    else:
        print("Penalty")