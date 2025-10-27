a = int(input())
b = float(input())
c = float(input())
cnt = a * (5280 / 3600) * c
print("MADE IT" if b <= cnt else "FAILED TEST")