a = input()
if a == '"':
    print("CE")
elif a == '""':
    print("CE")
elif a[0] == '"' and a[-1] == '"':
    print(a[1:-1])
elif a == "":
    print("CE")
else:
    print("CE")