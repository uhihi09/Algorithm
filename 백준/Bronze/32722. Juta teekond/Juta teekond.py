def find(a,b,c):
    if a == 1:
        if b == 6:
            if c == 2:
                return "JAH"
            elif c == 5:
                return "JAH"
        elif b == 8:
            if c == 2:
                return "JAH"
            elif c == 5:
                return "JAH"
    elif a == 3:
        if b == 6:
            if c == 2:
                return "JAH"
            elif c == 5:
                return "JAH"
        elif b == 8:
            if c == 2:
                return "JAH"
            elif c == 5:
                return "JAH"
    return "EI"


a = int(input())
b = int(input())
c = int(input())
print(find(a,b,c))