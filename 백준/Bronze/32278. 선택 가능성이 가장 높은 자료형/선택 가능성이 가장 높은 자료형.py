a = int(input())
if a >= -32768 and a <= 32767:
    print("short")
elif a >= -2147483648 and a <= 2147483647:
    print("int")
else:
    print("long long")