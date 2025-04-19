n = int(input())
p = int(input())
if n >= 5 and n < 10:
    if 500 > p:
        print(0)
    else:
        print(p-500)
elif n >= 10 and n < 15:
    if p > 5000:
        print(int(p*(90/100)))
    elif 500 > p:
        print(0)
    else:
        print(p-500)
elif n >= 15 and n < 20:
    if p > 20000:
        print(int(p*(90/100)))
    elif 2000 > p:
        print(0)
    else:
        print(p-2000)
elif n >= 20:
    if p > 8000:
        print(int(p*(75/100)))
    elif 2000 > p:
        print(0)
    else:
        print(p-2000)
elif n == 0:
    print(p)
else:
    print(p)